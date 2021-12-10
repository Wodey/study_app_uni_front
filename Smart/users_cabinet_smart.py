from Dumb.users_cabinet import Ui_Form as Dumb_users_cabinet
from PyQt5 import QtWidgets
import sys

class Users_cabinet_smart(QtWidgets.QMainWindow, Dumb_users_cabinet):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.pushButton.clicked.connect(self.prev_page)
    def prev_page(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Users_cabinet_smart()
    window.show()
    app.exec_()