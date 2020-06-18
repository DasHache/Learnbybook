import sys
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QStatusBar, QToolBar, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen



def test_button_clicked():
    print("test_button_clicked")

class View(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Hangman')
        self.setGeometry(100, 100, 800, 700)

        self.my_widget = QWidget(self)
        self.setCentralWidget(self.my_widget)

        self.my_layout = QVBoxLayout()
        self.my_widget.setLayout(self.my_layout)

        self.create_button()
        self.createWordLineEdit()
        self.create_buttons()
        self.drawline()



    def create_button(self):
        self.button = QPushButton("X", self.my_widget)
        #self.button.setGeometry(300, 300, 100, 100)
        self.button.move(670, 20)
        self.button.setFixedSize(100, 100)
        #self.my_layout.addWidget(self.button)

    def create_buttons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()

        buttonsLayout.
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

    def createWordLineEdit(self):
        self.word_LineEdit = QLineEdit("", self.my_widget)
        #self.word_LineEdit.setFixedHeight(300)
        #self.word_LineEdit.setFixedWidth(600)
        self.word_LineEdit.setFixedSize(600, 40)
        self.word_LineEdit.move(20, 20)
        #self.word_LineEdit.setFont(QFont('NewTimesRoman', 30))
        self.word_LineEdit.setAlignment(Qt.AlignLeft)
        self.word_LineEdit.setPlaceholderText("Enter a word to guess and press 'Enter'...")
        self.word_LineEdit.setReadOnly(False)
        #self.my_layout.addWidget(self.word_LineEdit)

    def drawline(self):
        painter = QPainter(self)
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.red)
        painter.setBrush(Qt.white)
        painter.drawLine(0, 0, 200, 200)

    def paintEvent(self, event):
        self.painter = QPainter(self)
        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(300, 100, 400, 200)

        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 195, 170, 220)

        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 195, 230, 220)

        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 270, 170, 350)

        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 270, 230, 350)
#
        self.painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        self.painter.drawEllipse(176, 150, 45, 45)
#
#    
        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 100, 400, 100)
#
#
        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(400, 100, 400, 400)
#
        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 100, 200, 150)
#
        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 195, 200, 270)
#
        self.painter.end()

class Controler:

    def __init__(self, model, view):
        self.my_model = model

        self.my_view = view
        self.my_view.word_LineEdit.returnPressed.connect(partial(self.save_new_word))

    def save_new_word(self):
        self.my_model.set_word(self.my_view.word_LineEdit.text())

        self.my_view.word_LineEdit.setVisible(False)


class Model:
    def __init__(self):
        self.word = "default"

    def set_word(self, new_word):
        self.word = new_word
        #print('New word to guess {' + self.word + '} has been saved')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    var_view = View()
    var_view.show()
    var_model = Model()
    Controler(model=var_model, view=var_view)
    sys.exit(app.exec_())
