from Dumb.admin_cabinet import Ui_Form
from PyQt5 import QtWidgets
import sys
from context import context
from Smart.create_task_smart import CreateTaskSmart
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class AdminCabinetSmart(QtWidgets.QWidget, Ui_Form):
    def __init__(self, widget=None):
        super().__init__()
        self.setupUi(self)
        self.tasks = []
        self.widget = widget
        self.pushButton_3.clicked.connect(self.widget.close)
        self.pushButton_2.clicked.connect(self.task_edit)
        self.pushButton_4.clicked.connect(self.endlesson)
        self.rerender()

    def endlesson(self):
        context.notify()
        self.widget.setCurrentIndex(3)

    def goto_edit_task(self, tid):
        task_id = tid
        def goto_edit_task_inner():
            self.task_edit(task_id)

        return goto_edit_task_inner

    def rerender(self):
        for index in range(6):
            try:
                lb = self.findChild(QtWidgets.QCommandLinkButton, f"commandLinkButton_{index + 1}")
                lb.hide()
            except:
                continue
        self.receive_tasks()

    def task_edit(self, tid=""):
        dialog = CreateTaskSmart(tid=tid)
        dialog.exec_()
        dialog.show()

    def receive_tasks(self):
        try:
            r = requests.get(f"{os.environ.get('URI')}/get_all_tasks")
            self.tasks = r.json()

            for index, i in enumerate(self.tasks):
                try:
                    lb = self.findChild(QtWidgets.QCommandLinkButton, f"commandLinkButton_{index + 1}")
                    lb.setText(f"{i['name']} - {i['score']}")
                    lb.clicked.connect(self.goto_edit_task(i['tid']))
                    lb.show()
                except:
                    continue
        except Exception as e:
            print(e)
            return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AdminCabinetSmart()
    window.show()
    app.exec_()
