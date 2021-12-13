from Dumb.admin_input import Ui_Form
from PyQt5 import QtWidgets
import sys
import json


class AdminInputSmart(QtWidgets.QWidget, Ui_Form):
    def __init__(self, widget=None):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.pushButton.clicked.connect(self.goto_2_input)
        self.pushButton_2.clicked.connect(self.goto_admin_page)

    def goto_2_input(self):
        self.widget.setCurrentIndex(0)

    def goto_admin_page(self):
        with open("admin.json", "w") as userf:
            json.dump({"name": self.textEdit.toPlainText()}, userf)
        self.widget.goto_2_main_component(2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AdminInputSmart()
    window.show()
    app.exec_()
