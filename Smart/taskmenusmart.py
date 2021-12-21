import imp
import json

from Dumb.task_menu import Ui_Form as TaskMenu
from Smart.taskmenuareyousuresmart import TaskMenuAreYouSureSmart as DialogWin
import sys
from PyQt5 import QtWidgets, QtCore


class TaskMenuSmart(QtWidgets.QWidget, TaskMenu):
    def __init__(self, widget=None):
        super().__init__()
        self.widget = widget
        self.recieve_data()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_dialog_win)
        self.pushButton_2.clicked.connect(self.goto_page_2)
        self.pushButton_3.clicked.connect(self.run_code)
        self.isCodeRunError = False
        _translate = QtCore.QCoreApplication.translate
        self.label_6.setText(_translate("Form", f"Для f({self.data['tests'][0]['argument']}): "))
        self.label_7.setText(_translate("Form", f"Ожидается: {self.data['tests'][0]['value']}"))
        self.label_9.setText(_translate("Form", f"Для f({self.data['tests'][1]['argument']}): "))
        self.label_8.setText(_translate("Form", f"Ожидается: {self.data['tests'][1]['value']}"))
        self.label_10.setText(_translate("Form", f"Для f({self.data['tests'][2]['argument']}): "))
        self.label_11.setText(_translate("Form", f"Ожидается: {self.data['tests'][2]['value']}"))

    def goto_page_2(self):
        self.widget.setCurrentIndex(1)

    @staticmethod
    def open_dialog_win():
        dialog = DialogWin()
        dialog.exec_()
        dialog.show()

    def recieve_data(self):
        with open("data.json") as dfile:
            self.data = json.load(dfile)

    def run_code(self):
        code = self.textEdit.toPlainText()
        _translate = QtCore.QCoreApplication.translate
        with open("code.py", "w") as codefile:
            codefile.writelines(code)
        try:
            import code
            imp.reload(code)
        except:
            self.isCodeRunError = True

        self.label_6.setText(
            f"Для f({self.data['tests'][0]['argument']}): {code.solution(self.data['tests'][0]['argument'])}")
        self.label_9.setText(
            f"Для f({self.data['tests'][1]['argument']}): {code.solution(self.data['tests'][1]['argument'])}")
        self.label_10.setText(
            f"Для f({self.data['tests'][2]['argument']}): {code.solution(self.data['tests'][2]['argument'])}")

        if self.data['tests'][0]['value'] == code.solution(self.data['tests'][0]['argument']):
            self.label_6.setStyleSheet("color: green")
        else:
            self.label_6.setStyleSheet("color: red")

        if self.data['tests'][1]['value'] == code.solution(self.data['tests'][1]['argument']):
            self.label_9.setStyleSheet("color: green")
        else:
            self.label_9.setStyleSheet("color: red")

        if self.data['tests'][2]['value'] == code.solution(self.data['tests'][2]['argument']):
            self.label_10.setStyleSheet("color: green")
        else:
            self.label_10.setStyleSheet("color: red")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TaskMenuSmart()
    window.show()
    app.exec_()
