import json
from Dumb.input import Ui_Input_win
from PyQt5 import QtWidgets
import sys
import requests
from context import context


class InputPageSmart(QtWidgets.QWidget, Ui_Input_win):
    def __init__(self, widget=None):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.pushButton_2.clicked.connect(self.goto_main_page)
        self.pushButton.clicked.connect(self.goto_input_page)
        self.isUserExist = False

    def goto_main_page(self):
        self.send_data_and_set_id()
        print('h1')
        if not self.isUserExist:
            print('h2')
            self.widget.goto_2_main_component()
        else:
            self.label_2.show()

    def goto_input_page(self):
        self.widget.setCurrentIndex(1)

    def send_data_and_set_id(self):
        print({"username": self.textEdit.toPlainText()})
        r = requests.post('http://127.0.0.1:5000/register', json={"username": self.textEdit.toPlainText()})
        if (cleaned_data := r.json()) == 1:
            self.isUserExist = True
            return
        self.isUserExist = False
        context.update_state({"uid": cleaned_data['uid'], "username": self.textEdit.toPlainText(), "score": 0})
        print(context.get_state())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = InputPageSmart()
    window.show()
    app.exec_()
