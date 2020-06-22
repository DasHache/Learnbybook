import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QStatusBar, QToolBar, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QBrush, QPen

class Window(QMainWindow):

    def __init__(self):

        super().__init__()

        self.title = "PyQt5 Drawing Tutorial"

        self.top= 150

        self.left= 150

        self.width = 500

        self.height = 500

        self.InitWindow()

    def InitWindow(self):

        self.setWindowTitle(self.title)

        self.setGeometry(self.top, self.left, self.width, self.height)

        self.show()



    def paintEvent(self, event):
        self.painter = QPainter(self)
        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(300, 100, 400, 200)

       # self.painter.setPen(QtCore.Qt.black)
       # self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 195, 170, 220)

       # self.painter.setPen(QtCore.Qt.black)
        #self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 195, 230, 220)

        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 270, 170, 350)

        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 270, 230, 350)

#horizontal

        self.painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        self.painter.drawEllipse(176, 150, 45, 45)

        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 100, 400, 100)


#vertical
        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(400, 100, 400, 400)

        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 100, 200, 150)

        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 195, 200, 270)

App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())

sys.exit(app.exec_())


def create_buttons(self):
    self.buttons = {}
    buttonsLayout = QGridLayout()
    buttons = {'a': (5, 0),
               'b': (5, 1),
               'c': (5, 2),
               'd': (5, 3),
               'e': (5, 4),
               'f': (5, 5),
               'g': (5, 6),
               'h': (5, 7),
               'i': (5, 8),
               'j': (5, 9),
               'k': (5, 10),
               'l': (5, 11),
               'm': (5, 12),
               'n': (6, 0),
               'o': (6, 1),
               'p': (6, 2),
               'q': (6, 3),
               'r': (6, 4),
               's': (6, 5),
               't': (6, 6),
               'u': (6, 7),
               'v': (6, 8),
               'w': (6, 9),
               'x': (6, 10),
               'y': (6, 11),
               'z': (6, 12),
               "'": (7, 6),
               '-': (7, 7),
               }

    for btnText, pos in buttons.items():
        self.buttons[btnText] = QPushButton(btnText)
        self.buttons[btnText].setFixedSize(60, 60)
        buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
    self.my_layout.addLayout(buttonsLayout)