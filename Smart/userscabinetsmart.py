from Dumb.users_cabinet import Ui_Form as Dumb_users_cabinet
from PyQt5 import QtWidgets
import sys
import requests
from context import context
from dotenv import load_dotenv
import os

# TODO new design in qt-designer
# TODO add timer in designer
# TODO add timer functionality

load_dotenv()

class UsersCabinetSmart(QtWidgets.QMainWindow, Dumb_users_cabinet):
    def __init__(self, widget=None):
        super().__init__()
        state = context.get_state()
        self.setupUi(self)
        self.tasks = []
        self.widget = widget
        self.receive_tasks()
        self.label_3.setText(str(state['score']))
        self.pushButton_3.clicked.connect(self.goto_page_1)
        for index, i in enumerate(self.tasks):
            lb = self.findChild(QtWidgets.QCommandLinkButton, f"commandLinkButton_{index + 1}")
            lb.setText(f"{i['name']} - {i['score']} баллов")
            lb.clicked.connect(self.goto_task(i['tid']))
            lb.show()

    def goto_task(self, tid):
        task_id = tid

        def goto_task_inner():
            context.update_state({"tid": task_id})
            self.widget.setCurrentIndex(1)

        return goto_task_inner

    def goto_page_1(self):
        self.widget.close()

    def receive_tasks(self):
        uid = context.get_state()['uid']
        try:
            r = requests.get(f"{os.environ.get('URI')}/get_tasks/{uid}")
            self.tasks = r.json()
        except:
            return

    def rerender(self):
        state = context.get_state()
        self.label_5.setText(state['username'])
        self.label_3.setText(str(state['score']))
        self.receive_tasks()


        for index in range(20):
            try:
                lb = self.findChild(QtWidgets.QCommandLinkButton, f"commandLinkButton_{index + 1}")
                lb.hide()
            except:
                continue

        for index in range(7, 17):
            try:
                lb = self.findChild(QtWidgets.QLabel, f"label_{index}")
                lb.hide()
            except:
                continue

        for index, i in enumerate(self.tasks):
            lb = self.findChild(QtWidgets.QCommandLinkButton, f"commandLinkButton_{index + 1}")
            lb.setText(f"{i['name']} - {i['score']} баллов")
            lb.clicked.connect(self.goto_task(i['tid']))
            lb.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UsersCabinetSmart()
    window.show()
    app.exec_()
