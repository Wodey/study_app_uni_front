from Dumb.input import Ui_Input_win
from PyQt5 import QtWidgets

class Input_page_smart(QtWidgets.QMainWindow, Ui_Input_win):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.next_page_2)
    def next_page_2(self):
        print("Hello")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Input_page_smart()
    window.show()
    app.exec_()