import sys
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QStatusBar, QToolBar, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtGui
from PyQt5 import QtCore
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

        self.create_buttons()
        self.create_button()
        self.createWordLineEdit()
        self.createLine()
        #self.button1.clicked.connect(partial(self.f_type, '1'))
        self.button2.clicked.connect(partial(self.f_type, '2'))
        self.button3.clicked.connect(self.f_type)
        self.button4.clicked.connect(self.f_type)
        self.button5.clicked.connect(self.f_type)
        self.button6.clicked.connect(self.f_type)
        self.button7.clicked.connect(self.f_type)
        self.button8.clicked.connect(self.f_type)
        self.button9.clicked.connect(self.f_type)
        self.button10.clicked.connect(self.f_type)
        self.button11.clicked.connect(self.f_type)
        self.button12.clicked.connect(self.f_type)
        self.button13.clicked.connect(self.f_type)
        self.button14.clicked.connect(self.f_type)
        self.button15.clicked.connect(self.f_type)
        self.button16.clicked.connect(self.f_type)
        self.button17.clicked.connect(self.f_type)
        self.button18.clicked.connect(self.f_type)
        self.button19.clicked.connect(self.f_type)
        self.button20.clicked.connect(self.f_type)
        self.button21.clicked.connect(self.f_type)
        self.button22.clicked.connect(self.f_type)
        self.button23.clicked.connect(self.f_type)
        self.button24.clicked.connect(self.f_type)
        self.button25.clicked.connect(self.f_type)
        self.button26.clicked.connect(self.f_type)
        self.button27.clicked.connect(self.f_type)
        self.button28.clicked.connect(self.f_type)

    def set_button_value(self, v):
        self.button.setText(v)


    def create_button(self):
        self.v = "10"
        self.button = QPushButton(self.v, self.my_widget)
        self.button.move(670, 20)
        self.button.setFixedSize(100, 100)

    def f_type(self, value):
        print("f_type called with value = ", value)

    def create_buttons(self):
        self.button1 = QPushButton("a", self.my_widget)
        self.button1.move(20, 500)
        self.button1.setFixedSize(50, 50)

        self.button2 = QPushButton("b", self.my_widget)
        self.button2.move(80, 500)
        self.button2.setFixedSize(50, 50)

        self.button3 = QPushButton("c", self.my_widget)
        self.button3.move(140, 500)
        self.button3.setFixedSize(50, 50)

        self.button4 = QPushButton("d", self.my_widget)
        self.button4.move(200, 500)
        self.button4.setFixedSize(50, 50)

        self.button5 = QPushButton("e", self.my_widget)
        self.button5.move(260, 500)
        self.button5.setFixedSize(50, 50)

        self.button6 = QPushButton("f", self.my_widget)
        self.button6.move(320, 500)
        self.button6.setFixedSize(50, 50)

        self.button7 = QPushButton("g", self.my_widget)
        self.button7.move(380, 500)
        self.button7.setFixedSize(50, 50)

        self.button8 = QPushButton("h", self.my_widget)
        self.button8.move(440, 500)
        self.button8.setFixedSize(50, 50)

        self.button9 = QPushButton("i", self.my_widget)
        self.button9.move(500, 500)
        self.button9.setFixedSize(50, 50)

        self.button10 = QPushButton("j", self.my_widget)
        self.button10.move(560, 500)
        self.button10.setFixedSize(50, 50)

        self.button11 = QPushButton("k", self.my_widget)
        self.button11.move(620, 500)
        self.button11.setFixedSize(50, 50)

        self.button12 = QPushButton("l", self.my_widget)
        self.button12.move(680, 500)
        self.button12.setFixedSize(50, 50)

        self.button13 = QPushButton("m", self.my_widget)
        self.button13.move(740, 500)
        self.button13.setFixedSize(50, 50)

        self.button14 = QPushButton("n", self.my_widget)
        self.button14.move(20, 560)
        self.button14.setFixedSize(50, 50)

        self.button15 = QPushButton("o", self.my_widget)
        self.button15.move(80, 560)
        self.button15.setFixedSize(50, 50)

        self.button16 = QPushButton("p", self.my_widget)
        self.button16.move(140, 560)
        self.button16.setFixedSize(50, 50)

        self.button17 = QPushButton("q", self.my_widget)
        self.button17.move(200, 560)
        self.button17.setFixedSize(50, 50)

        self.button18 = QPushButton("r", self.my_widget)
        self.button18.move(260, 560)
        self.button18.setFixedSize(50, 50)

        self.button19 = QPushButton("s", self.my_widget)
        self.button19.move(320, 560)
        self.button19.setFixedSize(50, 50)

        self.button20 = QPushButton("t", self.my_widget)
        self.button20.move(380, 560)
        self.button20.setFixedSize(50, 50)

        self.button21 = QPushButton("u", self.my_widget)
        self.button21.move(440, 560)
        self.button21.setFixedSize(50, 50)

        self.button22 = QPushButton("v", self.my_widget)
        self.button22.move(500, 560)
        self.button22.setFixedSize(50, 50)

        self.button23 = QPushButton("w", self.my_widget)
        self.button23.move(560, 560)
        self.button23.setFixedSize(50, 50)

        self.button24 = QPushButton("x", self.my_widget)
        self.button24.move(620, 560)
        self.button24.setFixedSize(50, 50)

        self.button25 = QPushButton("y", self.my_widget)
        self.button25.move(680, 560)
        self.button25.setFixedSize(50, 50)

        self.button26 = QPushButton("z", self.my_widget)
        self.button26.move(740, 560)
        self.button26.setFixedSize(50, 50)

        self.button27 = QPushButton("-", self.my_widget)
        self.button27.move(320, 620)
        self.button27.setFixedSize(50, 50)

        self.button28 = QPushButton("'", self.my_widget)
        self.button28.move(440, 620)
        self.button28.setFixedSize(50, 50)

    def createWordLineEdit(self):
        self.word_LineEdit = QLineEdit("", self.my_widget)
        # self.word_LineEdit.setFixedHeight(300)
        # self.word_LineEdit.setFixedWidth(600)
        self.word_LineEdit.setFixedSize(600, 40)
        self.word_LineEdit.move(20, 20)
        # self.word_LineEdit.setFont(QFont('NewTimesRoman', 30))
        self.word_LineEdit.setAlignment(Qt.AlignLeft)
        self.word_LineEdit.setPlaceholderText("Enter a word to guess and press 'Enter'...")
        self.word_LineEdit.setReadOnly(False)
        # self.my_layout.addWidget(self.word_LineEdit)

    def createLine(self):
        self.word2_LineEdit = QLineEdit("", self.my_widget)

        self.word2_LineEdit.setFixedSize(600, 40)
        self.word2_LineEdit.move(20, 20)

        self.word2_LineEdit.setAlignment(Qt.AlignLeft)
        self.word2_LineEdit.setPlaceholderText("_______")
        self.word2_LineEdit.setReadOnly(True)
        self.word2_LineEdit.setVisible(False)


    def paintEvent(self, event):
        self.painter = QPainter(self)
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

        view.button1.clicked.connect(partial(self.f_type_in_controller, '1'))
        #view.button1.clicked.connect(self.button_text())

        view.button2.clicked.connect(partial(self.my_view.set_button_value, '111'))

    def f_type_in_controller(self, value):
        print("f_type_in_controller with value = ", value, " with counter = ", self.my_model.counter)
        self.my_model.counter -= 1

    def button_text(self):
        self.vv = 10
        self.vv = self.vv - 1

        if self.vv == 9:
            self.my_view.button.setText("9")

        if self.vv == 8:
            self.my_view.button.setText("8")

        if self.vv == 7:
            self.my_view.button.setText("7")

        if self.vv == 6:
            self.my_view.button.setText("6")

        if self.vv == 5:
            self.my_view.button.setText("5")

        if self.vv == 4:
            self.my_view.button.setText("4")

        if self.vv == 3:
            self.my_view.button.setText("3")

        if self.vv == 2:
            self.my_view.button.setText("2")

        if self.vv == 1:
            self.my_view.button.setText("1")

        if self.vv == 0:
            self.my_view.button.setText("0")



    def save_new_word(self):
        self.my_model.set_word(self.my_view.word_LineEdit.text())

        self.my_view.word_LineEdit.setVisible(False)
        self.my_view.word2_LineEdit.setVisible(True)


class Model:
    def __init__(self):
        self.word = "default"
        self.counter = 10

    def set_word(self, new_word):
        self.word = new_word
        # print('New word to guess {' + self.word + '} has been saved')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    var_view = View()
    var_view.show()
    var_model = Model()
    Controler(model=var_model, view=var_view)
    sys.exit(app.exec_())
