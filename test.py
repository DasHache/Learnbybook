import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QStatusBar, QToolBar, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QBrush, QPen

class View(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Hangman')
        self.setGeometry(100, 100, 800, 700)

        self.my_widget = QWidget(self)
        self.setCentralWidget(self.my_widget)

        self.my_layout = QVBoxLayout()
        self.my_widget.setLayout(self.my_layout)
        self.drawline()



    def drawline(self):
        self.painter = QPainter(self)
        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.setPen(QtCore.Qt.red)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(0, 0, 200, 200)



app = QApplication(sys.argv)
var_view = View()
var_view.show()

sys.exit(app.exec_())