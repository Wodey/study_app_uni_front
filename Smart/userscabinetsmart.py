from Dumb.users_cabinet import Ui_Form as Dumb_users_cabinet
from PyQt5 import QtWidgets
import sys
import requests
from context import context
from dotenv import load_dotenv
import os
from utilities.interval import set_interval

# TODO new design in qt-designer
# TODO add timer in designer
# TODO add timer functionality

load_dotenv()


class UsersCabinetSmart(QtWidgets.QMainWindow, Dumb_users_cabinet):
    def __init__(self, widget=None):
        super().__init__()
        self.users = [
            {
                "name": "Ivan",
                "score": 10
            },
            {
                "name": "Vanya",
                "score": 9
            },
            {
                "name": "Vanya",
                "score": 8
            },
            {
                "name": "Vanya",
                "score": 7
            },
            {
                "name": "Vanya",
                "score": 6
            },
            {
                "name": "Vanya",
                "score": 5
            },
            {
                "name": "Vanya",
                "score": 4
            },
            {
                "name": "Vanya",
                "score": 3
            },
            {
                "name": "Vanya",
                "score": 2
            },
            {
                "name": "Vanya",
                "score": 1
            }
        ]
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

    def receive_users(self):
        try:
            r = requests.get(f"{os.environ.get('URI')}/admin/get_scores_table")
            if (raw_r := r.json()) == "1":
                raise "Error 1 in receive_users"
            self.users = raw_r['body']
            print(raw_r)
        except Exception as e:
            print(f"score_page_smart {e}")
            return

    def update_users_scores(self):
        for index in range(7, 17):
            try:
                lb = self.findChild(QtWidgets.QLabel, f"label_{index}")
                lb.hide()
            except:
                continue
        self.receive_users()

        for index, i in enumerate(self.users):
            try:
                lb = self.findChild(QtWidgets.QLabel, f"label_{index + 7}")
                lb.setText(f"{index + 1}. {i['name']} - {i['score']}")
                lb.show()
            except:
                continue

    def rerender(self):
        state = context.get_state()
        self.label_5.setText(state['username'])
        self.label_3.setText(str(state['score']))
        self.receive_tasks()
        self.update_users_scores()
        for index in range(20):
            try:
                lb = self.findChild(QtWidgets.QCommandLinkButton, f"commandLinkButton_{index + 1}")
                lb.hide()
            except:
                continue


        for index, i in enumerate(self.tasks):
            lb = self.findChild(QtWidgets.QCommandLinkButton, f"commandLinkButton_{index + 1}")
            lb.setText(f"{i['name']} - {i['score']} баллов")
            lb.clicked.connect(self.goto_task(i['tid']))
            lb.show()

        set_interval(self.update_users_scores, 60)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UsersCabinetSmart()
    window.show()
    app.exec_()
