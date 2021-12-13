from Dumb.admin_input import Ui_Form
from PyQt5 import QtWidgets
import sys


# TODO Read a data from input form and save it
class AdminInputSmart(QtWidgets.QWidget, Ui_Form):
    def __init__(self, widget=None):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.pushButton.clicked.connect(self.goto_2_input)

    def goto_2_input(self):
        self.widget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AdminInputSmart()
    window.show()
    app.exec_()
