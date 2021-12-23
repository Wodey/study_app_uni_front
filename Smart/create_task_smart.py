from Dumb.create_task import Ui_Dialog
from PyQt5 import QtWidgets
import requests
import sys
from dotenv import load_dotenv
import os
from context import context
import json
load_dotenv()

class CreateTaskSmart(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, tid=""):
        super().__init__()
        self.setupUi(self)
        self.tid = tid
        self.data = {}
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.send_data)
        if tid:
            self.receive_task()
            self.pushButton_2.setEnabled(True)
            self.lineEdit.setText(self.data['name'])
            self.textEdit.setText(self.data['body'])
            self.lineEdit_2.setText(' '.join(map(str, self.data['tests'][0]['arguments'])))
            self.lineEdit_3.setText(str(self.data['tests'][0]['value']))
            self.lineEdit_4.setText(' '.join(map(str, self.data['tests'][1]['arguments'])))
            self.lineEdit_5.setText(str(self.data['tests'][1]['value']))
            self.lineEdit_6.setText(' '.join(map(str, self.data['tests'][2]['arguments'])))
            self.lineEdit_7.setText(str(self.data['tests'][2]['value']))
            self.spinBox.setValue(int(self.data['score']))
            self.spinBox_2.setValue(int(self.data['arguments_count']))

    def delete(self):
        try:
            requests.get(f"{os.environ.get('URI')}/admin/delete_task/{self.tid}")
            context.notify()
            self.close()
        except Exception as e:
            print(f'Delition expectations is {e}')
    def receive_task(self):
        try:
            r = requests.get(f"{os.environ.get('URI')}/get_task/{self.tid}")
            self.data = r.json()
        except Exception as e:
            print('receive task exc')
            print(e)
            return

    def send_data(self):
        new_data = {}
        new_data["name"] = self.lineEdit.text()
        new_data["body"] = self.textEdit.toPlainText()
        new_data["tests"] = []
        new_data["tests"].append(
            {"arguments": list(map(int, self.lineEdit_2.text().split(' '))), "value": int(self.lineEdit_3.text())})
        new_data["tests"].append(
            {"arguments": list(map(int, self.lineEdit_4.text().split(' '))), "value": int(self.lineEdit_5.text())})
        new_data['tests'].append(
            {"arguments": list(map(int, self.lineEdit_6.text().split(' '))), "value": int(self.lineEdit_7.text())})

        new_data["score"] = self.spinBox.value()
        new_data["arguments_count"] = self.spinBox_2.value()
        new_data["initial"] = f"def solution({', '.join([chr(i + 97) for i in range(self.spinBox_2.value())])}):"

        if self.tid:
            try:
                r = requests.post(f'{os.environ.get("URI")}/admin/update_task/{self.tid}', json=new_data)
                context.notify()
                self.close()
            except Exception as e:
                print(e)
                return
        else:
            try:
                r = requests.post(f'{os.environ.get("URI")}/admin/add_task', json=new_data)
                context.notify()
                self.close()
            except Exception as e:
                print(f"else exception {e}")
                return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CreateTaskSmart()
    window.show()
    app.exec_()
