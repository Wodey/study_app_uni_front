from Dumb.users_cabinet import Ui_Form as Dumb_users_cabinet
from PyQt5 import QtWidgets
import sys
import requests
from context import context

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
        self.tasks = []
        self.widget = widget
        self.receive_tasks()
        self.pushButton.clicked.connect(self.goto_page_1)

        for index, i in enumerate(self.tasks):
            lb = self.findChild(QtWidgets.QCommandLinkButton, f"commandLinkButton_{index + 1}")
            lb.setText(f"{i['name']} - {i['score']} баллов")
            lb.show()
    def goto_page_1(self):
        self.widget.close()

    def receive_tasks(self):
        r = requests.get("http://127.0.0.1:5000/get_tasks/61c23866b167e66f2988147a")
        self.tasks = r.json()

    def rerender(self):
        state = context.get_state()
        self.label_5.setText(state['username'])
        print(f"users cabinet state {state} ")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UsersCabinetSmart()
    window.show()
    app.exec_()
