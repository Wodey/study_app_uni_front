from Dumb.input import Ui_Input_win
from PyQt5 import QtWidgets
import sys

class Input_page_smart(QtWidgets.QWidget, Ui_Input_win):
    def __init__(self, widget=None):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.pushButton_2.clicked.connect(self.goto_page_2)
    def goto_page_2(self):
        self.widget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Input_page_smart()
    window.show()
    app.exec_()