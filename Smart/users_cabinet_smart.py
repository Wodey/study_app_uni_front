from Dumb.users_cabinet import Ui_Form as Dumb_users_cabinet
from PyQt5 import QtWidgets
import sys

class Users_cabinet_smart(QtWidgets.QMainWindow, Dumb_users_cabinet):
    def __init__(self, widget=None):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.pushButton.clicked.connect(self.goto_page_1)
    def goto_page_1(self):
        self.widget.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Users_cabinet_smart()
    window.show()
    app.exec_()