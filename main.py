from input import Ui_Input_win as InputPage
import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
page1 = QtWidgets.QWidget()
ui = InputPage()
ui.setupUi(page1)
page1.show()

sys.exit(app.exec_())

