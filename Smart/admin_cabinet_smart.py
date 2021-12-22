from Dumb.admin_cabinet import Ui_Form
from PyQt5 import QtWidgets
import sys
from context import context


# TODO Redesign a dump component
class AdminCabinetSmart(QtWidgets.QWidget, Ui_Form):
    def __init__(self, widget=None):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.pushButton_2.clicked.connect(self.widget.close)

    def rerender(self):
        state = context.get_state()
        print(f"admin cabine state {state}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AdminCabinetSmart()
    window.show()
    app.exec_()
