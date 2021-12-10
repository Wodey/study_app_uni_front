from Dumb.task_menu import Ui_Form as TaskMenu
from Smart.taskmenuareyousuresmart import TaskMenuAreYouSureSmart as DialogWin
import sys
from PyQt5 import QtWidgets


# TODO read name,body, tests of function from the file
# TODO write code from input to file on the send button
# TODO add run test button in designer
# TODO add a way to run a function from the code with test arguments

class TaskMenuSmart(QtWidgets.QWidget, TaskMenu):
    def __init__(self, widget=None):
        super().__init__()
        self.widget = widget
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_dialog_win)
        self.pushButton_2.clicked.connect(self.goto_page_2)

    def goto_page_2(self):
        self.widget.setCurrentIndex(1)

    @staticmethod
    def open_dialog_win():
        dialog = DialogWin()
        dialog.exec_()
        dialog.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TaskMenuSmart()
    window.show()
    app.exec_()
