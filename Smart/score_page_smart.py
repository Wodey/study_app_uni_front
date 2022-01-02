from Dumb.score_page import Ui_Form
from PyQt5 import QtWidgets
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class ScorePageSmart(QtWidgets.QWidget, Ui_Form):
    def __init__(self, widget=None):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.pushButton.clicked.connect(lambda: self.widget.close())
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

        self.rerender()

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

    def rerender(self):
        self.receive_users()
        print(self.users)
        for index in range(12):
            try:
                lb = self.findChild(QtWidgets.QLabel, f"label_{index + 1}")
                lb.hide()
            except:
                continue

        for index, i in enumerate(self.users[::-1]):
            try:
                lb = self.findChild(QtWidgets.QLabel, f"label_{index + 1}")
                lb.setText(f"{index + 1}. {i['name']} - {i['score']}")
                lb.show()
            except:
                continue
