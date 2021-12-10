from Smart.input_smart import Input_page_smart as FirstPage
import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = FirstPage()
window.show()

sys.exit(app.exec_())

