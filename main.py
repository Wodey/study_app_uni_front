from Smart.input_smart import Input_page_smart as FirstPage
from Smart.users_cabinet_smart import Users_cabinet_smart as SecondPage
from Smart.task_menu_smart import Task_menu_smart as ThirdPage
import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

page_1 = FirstPage(widget)
page_2 = SecondPage(widget)
page_3 = ThirdPage(widget)

widget.addWidget(page_1)
widget.addWidget(page_2)
widget.addWidget(page_3)

widget.show()
widget.setFixedWidth(1000)
widget.setFixedHeight(700)
sys.exit(app.exec_())

