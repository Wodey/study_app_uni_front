from Smart.input_smart import InputPageSmart as FirstPage
from Smart.userscabinetsmart import UsersCabinetSmart as SecondPage
from Smart.taskmenusmart import TaskMenuSmart as ThirdPage
from Smart.admin_input_smart import AdminInputSmart
import sys
from PyQt5 import QtWidgets

#python -m PyQt5.uic.pyuic -x admin_input.ui -o admin_input.py

class MainComponent(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        page_2 = SecondPage(self)
        page_3 = ThirdPage(self)

        self.addWidget(page_2)
        self.addWidget(page_3)

        self.setFixedWidth(1000)
        self.setFixedHeight(700)

class InputWidgets(QtWidgets.QStackedWidget):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        page_1 = FirstPage(self)
        page_2 = AdminInputSmart(self)

        self.addWidget(page_1)
        self.addWidget(page_2)

        self.setFixedWidth(400)
        self.setFixedHeight(400)

    def goto_2_main_component(self):
        self.widget.show()
        self.close()

app = QtWidgets.QApplication(sys.argv)

widget = MainComponent()

start_page = InputWidgets(widget)
start_page.show()

sys.exit(app.exec_())
