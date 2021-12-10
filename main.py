from Smart.input_smart import Input_page_smart as FirstPage
from Smart.users_cabinet_smart import Users_cabinet_smart as SecondPage
from Smart.task_menu_smart import Task_menu_smart as ThirdPage
import sys
from PyQt5 import QtWidgets

class MainComponent(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        page_2 = SecondPage(self)
        page_3 = ThirdPage(self)

        self.addWidget(page_2)
        self.addWidget(page_3)

        self.setFixedWidth(1000)
        self.setFixedHeight(700)

app = QtWidgets.QApplication(sys.argv)

widget = MainComponent()

page_1 = FirstPage(widget)
page_1.show()

sys.exit(app.exec_())

