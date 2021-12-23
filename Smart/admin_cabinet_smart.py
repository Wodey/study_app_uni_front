from Dumb.admin_cabinet import Ui_Form
from PyQt5 import QtWidgets
import sys
from context import context
from Smart.create_task_smart import CreateTaskSmart

class AdminCabinetSmart(QtWidgets.QWidget, Ui_Form):
    def __init__(self, widget=None):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.pushButton_3.clicked.connect(self.widget.close)
        self.pushButton_2.clicked.connect(self.task_edit)

    def rerender(self):
        state = context.get_state()
        print(f"admin cabine state {state}")
    def task_edit(self):
        dialog = CreateTaskSmart(tid="61c237c9b167e66f29881479")
        dialog.exec_()
        dialog.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AdminCabinetSmart()
    window.show()
    app.exec_()
