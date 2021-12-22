import imp
import json
import requests
from context import context
from Dumb.task_menu import Ui_Form as TaskMenu
from Smart.taskmenuareyousuresmart import TaskMenuAreYouSureSmart as DialogWin
import sys
from PyQt5 import QtWidgets, QtCore


class TaskMenuSmart(QtWidgets.QWidget, TaskMenu):
    def __init__(self, widget=None):
        super().__init__()
        self.widget = widget
        self.tid = ""
        self.data = {
            "score": 0,
            "name": None,
            "body": None,
            "initial": None,
            "tests": [
                {
                    "value": None,
                    "arguments": [None]
                },
                {
                    "value": None,
                    "arguments": [None]
                },
                {
                    "value": None,
                    "arguments": [None]
                }
            ]
        }
        self.recieve_data()
        self.setupUi(self)
        self.label_14.hide()
        self.pushButton.clicked.connect(self.open_dialog_win)
        self.pushButton_2.clicked.connect(self.goto_page_2)
        self.pushButton_3.clicked.connect(self.run_code)
        self.isCodeRunError = False
        self.sol1 = ''
        self.sol2 = ''
        self.sol3 = ''
        self.pushButton_4.clicked.connect(self.backToInitial)

    def goto_page_2(self):
        self.widget.setCurrentIndex(1)

    def backToInitial(self):
        self.textEdit.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
            f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{self.data['initial']}</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\t#Пишите код здесь,</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\t#Вам надо, чтобы ваша функция возвращала\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\t#определенное значение, также нельзя менять ее"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\t#название и сигнатуру</p>"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\treturn 0</p></body></html>")

    @staticmethod
    def open_dialog_win():
        dialog = DialogWin()
        dialog.exec_()
        dialog.show()

    def setup_dynamic_content(self):
        self.label_13.setText(f"{self.data['score']} баллов")
        self.label_2.setText(self.data['name'])
        self.textBrowser.setText(self.data['body'])

        self.textEdit.setHtml(
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                         f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{self.data['initial']}</p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\t#Пишите код здесь,</p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\t#Вам надо, чтобы ваша функция возвращала\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\t#определенное значение, также нельзя менять ее"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\t#название и сигнатуру</p></body></html>"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\treturn 0</p></body></html>"                                         )

        self.label_6.setText(f"Для f({self.data['tests'][0]['arguments']}): ")
        self.label_7.setText(f"Ожидается: {self.data['tests'][0]['value']}")
        self.label_9.setText("Form", f"Для f({self.data['tests'][1]['arguments']}): ")
        self.label_8.setText(f"Ожидается: {self.data['tests'][1]['value']}")
        self.label_10.setText(f"Для f({self.data['tests'][2]['arguments']}): ")
        self.label_11.setText(f"Ожидается: {self.data['tests'][2]['value']}")

    def recieve_data(self):
        try:
            r = requests.get(f"http://127.0.0.1:5000/get_task/{self.tid}")
            self.data = r.json()
            self.setup_dynamic_content()

        except:
            return

    def run_code(self):
        code = self.textEdit.toPlainText()
        _translate = QtCore.QCoreApplication.translate
        with open("code.py", "w") as codefile:
            codefile.writelines(code)
        try:
            import code
            imp.reload(code)
            self.sol1 = code.solution(*self.data['tests'][0]['arguments'])
            self.sol2 = code.solution(*self.data['tests'][1]['arguments'])
            self.sol3 = code.solution(*self.data['tests'][2]['arguments'])
        except:
            self.isCodeRunError = True
        else:
            self.isCodeRunError = False
        if self.isCodeRunError:
            self.label_14.show()
        self.label_6.setText(
            f"Для f({self.data['tests'][0]['arguments']}): {self.sol1}")
        self.label_9.setText(
            f"Для f({self.data['tests'][1]['arguments']}): {self.sol2}")
        self.label_10.setText(
            f"Для f({self.data['tests'][2]['arguments']}): {self.sol3}")

        if self.data['tests'][0]['value'] == self.sol1:
            self.label_6.setStyleSheet("color: green")
        else:
            self.label_6.setStyleSheet("color: red")

        if self.data['tests'][1]['value'] == self.sol2:
            self.label_9.setStyleSheet("color: green")
        else:
            self.label_9.setStyleSheet("color: red")

        if self.data['tests'][2]['value'] == self.sol3:
            self.label_10.setStyleSheet("color: green")
        else:
            self.label_10.setStyleSheet("color: red")

    def rerender(self):
        state = context.get_state()
        print(f"task menu state {state}")
        self.tid = state['tid']
        self.recieve_data()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TaskMenuSmart()
    window.show()
    app.exec_()
