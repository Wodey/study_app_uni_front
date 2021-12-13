import json

from Dumb.input import Ui_Input_win
from PyQt5 import QtWidgets
import sys



class InputPageSmart(QtWidgets.QWidget, Ui_Input_win):
    def __init__(self, widget=None):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.pushButton_2.clicked.connect(self.goto_main_page)
        self.pushButton.clicked.connect(self.goto_input_page)
    def goto_main_page(self):
        with open("user.json", "w") as userf:
            json.dump({"name": self.textEdit.toPlainText()}, userf)
        self.widget.goto_2_main_component()

    def goto_input_page(self):
        self.widget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = InputPageSmart()
    window.show()
    app.exec_()
