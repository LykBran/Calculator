from form_ui import Ui_Form
from PySide6.QtWidgets import QWidget, QApplication
import sys


class Form(QWidget):

    def __init__(self):
        super().__init__()
        self.calculation = ''
        self.result = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_0.clicked.connect(lambda: self.calculation_update(0))
        self.ui.pushButton_1.clicked.connect(lambda: self.calculation_update(1))
        self.ui.pushButton_2.clicked.connect(lambda: self.calculation_update(2))
        self.ui.pushButton_3.clicked.connect(lambda: self.calculation_update(3))
        self.ui.pushButton_4.clicked.connect(lambda: self.calculation_update(4))
        self.ui.pushButton_5.clicked.connect(lambda: self.calculation_update(5))
        self.ui.pushButton_6.clicked.connect(lambda: self.calculation_update(6))
        self.ui.pushButton_7.clicked.connect(lambda: self.calculation_update(7))
        self.ui.pushButton_8.clicked.connect(lambda: self.calculation_update(8))
        self.ui.pushButton_9.clicked.connect(lambda: self.calculation_update(9))
        self.ui.pushButton_add.clicked.connect(lambda: self.calculation_update("+"))
        self.ui.pushButton_sub.clicked.connect(lambda: self.calculation_update("-"))
        self.ui.pushButton_mul.clicked.connect(lambda: self.calculation_update("*"))
        self.ui.pushButton_div.clicked.connect(lambda: self.calculation_update("/"))
        self.ui.pushButton_point.clicked.connect(lambda: self.calculation_update("."))
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_calculate.clicked.connect(self.calculate)
        self.ui.pushButton_clear.clicked.connect(self.clear)

    def calculation_update(self, c: int | str):
        self.calculation += str(c)
        self.ui.lineEdit.setText(self.calculation)

    def calculate(self):
        if self.calculation:
            result = eval(self.calculation)
            self.calculation = str(result)
            self.ui.lineEdit.setText(self.calculation)

    def back(self):
        if self.calculation:
            self.calculation = self.calculation[:-1]
            self.ui.lineEdit.setText(self.calculation)

    def clear(self):
        self.calculation = ""
        self.ui.lineEdit.setText(self.calculation)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec())
