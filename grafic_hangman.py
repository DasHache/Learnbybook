import sys
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QStatusBar, QToolBar, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5 import QtCore



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
        buttons = {'a': (0, 0),
                   'b': (0, 1),
                   'c': (0, 2),
                   'd': (0, 3),
                   'e': (0, 4),
                   'f': (0, 5),
                   'g': (0, 6),
                   'h': (0, 7),
                   'i': (0, 8),
                   'j': (0, 9),
                   'k': (0, 10),
                   'l': (0, 11),
                   'm': (0, 12),
                   'n': (1, 0),
                   'o': (1, 1),
                   'p': (1, 2),
                   'q': (1, 3),
                   'r': (1, 4),
                   's': (1, 5),
                   't': (1, 6),
                   'u': (1, 7),
                   'v': (1, 8),
                   'w': (1, 9),
                   'x': (1, 10),
                   'y': (1, 11),
                   'z': (1, 12),
                   "'": (2, 6),
                   '-': (2, 7),
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

        self.painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        self.painter.drawEllipse(176, 150, 45, 45)

        # horizontal
        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 100, 400, 100)

        # vertical
        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(400, 100, 400, 400)

        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 100, 200, 150)

        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawLine(200, 195, 200, 270)


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
