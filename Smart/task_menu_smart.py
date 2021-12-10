from Dumb.task_menu import Ui_Form as TaskMenu
from Smart.task_menu_are_you_sure_smart import Task_menu_are_you_sure_smart as DialogWin
import sys
from PyQt5 import QtWidgets

class Task_menu_smart(QtWidgets.QWidget, TaskMenu):
    def __init__(self, widget=None):
        super().__init__()
        self.widget = widget
        self.setupUi(self)
        self.pushButton.clicked.connect(self.OpenDialogWin)
        self.pushButton_2.clicked.connect(self.goto_page_2)
    def goto_page_2(self):
        self.widget.setCurrentIndex(1)
    def OpenDialogWin(self):
        dialog = DialogWin()
        dialog.exec_()
        dialog.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Task_menu_smart()
    window.show()
    app.exec_()