from Dumb.task_menu_are_you_sure import Ui_Form as TaskMenuAreYouSure
import sys
from PyQt5 import QtWidgets
import requests
from context import context
import os
from dotenv import load_dotenv

load_dotenv()


class TaskMenuAreYouSureSmart(QtWidgets.QDialog, TaskMenuAreYouSure):
    def __init__(self, data, cb):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.send)
        self.data = data
        self.close_parent = cb

    def send(self):
        # TODO send a data to server
        state = context.get_state()
        uid = state['uid']
        score = state['score']
        r = requests.post(f"{os.environ.get('URI')}/deliver_task/{uid}", json=self.data)
        print(f"r is {r.json()}")
        if r.json() == 0:
            context.update_state({"score": score + self.data['score']})
            self.close_parent()
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TaskMenuAreYouSureSmart()
    window.show()
    app.exec_()
