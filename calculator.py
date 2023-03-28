import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

import ui
from ui import Ui_MainWindow


class Calc(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Ui()


    def Ui(self):
        self.setWindowTitle('calculator')
        self.ui.plus.clicked.connect(self.pls)
        self.ui.minus.clicked.connect(self.mns)

    def pls(self):
        number = int(self.ui.number.text())
        number2 = int(self.ui.number2.text())
        a = (number + number2)
        self.ui.number2_2.setText(str(a))


    def mns(self):
        number = int(self.ui.number.text())
        number2 = int(self.ui.number2.text())
        b = (number - number2)
        self.ui.number2_2.setText(str(b))





app = QtWidgets.QApplication([])
application = Calc()
application.show()
sys.exit(app.exec())