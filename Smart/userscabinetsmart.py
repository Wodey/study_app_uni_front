from Dumb.users_cabinet import Ui_Form as Dumb_users_cabinet
from PyQt5 import QtWidgets
import sys


# TODO Read list from the file and generate on its basis a list with links to task_menu
# TODO new design in qt-designer
# TODO Read information about user from the file
# TODO add "сдаюсь" button functionality and a page for it of course
# TODO add timer in designer
# TODO add timer functionality

class UsersCabinetSmart(QtWidgets.QMainWindow, Dumb_users_cabinet):
    def __init__(self, widget=None):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.pushButton.clicked.connect(self.goto_page_1)

    def goto_page_1(self):
        self.widget.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UsersCabinetSmart()
    window.show()
    app.exec_()
