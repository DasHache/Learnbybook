import sys
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QPen


class View(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Hangman')
        self.setGeometry(100, 100, 800, 700)

        self.my_widget = QWidget(self)
        self.setCentralWidget(self.my_widget)

        self.my_layout = QVBoxLayout()
        self.my_widget.setLayout(self.my_layout)

        self.counter = 10

        self.create_buttons()
        self.create_button()
        self.createWordLineEdit()
        self.createLine()
        self.createlw()
        self.createyesno()
        self.j1but()
        self.j2but()


    def j1but(self):
        self.j1 = QPushButton('0', self.my_widget)
        self.j1.setStyleSheet("background-color: red")
        self.j1.move(710, 200)
        self.j1.setFixedSize(50, 50)

    def j2but(self):
        self.j2 = QPushButton('0', self.my_widget)
        self.j2.setStyleSheet("background-color: blue")
        self.j2.move(710, 270)
        self.j2.setFixedSize(50, 50)


# yes no buttons
    def createyesno(self):
        self.buttonno = QPushButton("No", self.my_widget)
        self.buttonno.move(470, 400)
        self.buttonno.setFixedSize(100, 50)
        self.buttonno.setVisible(False)

        self.buttonyes = QPushButton('Yes', self.my_widget)
        self.buttonyes.move(250, 400)
        self.buttonyes.setFixedSize(100, 50)
        self.buttonyes.setVisible(False)

# loose or win button
    def createlw(self):
        self.buttonlw = QPushButton('', self.my_widget)
        self.buttonlw.move(155, 280)
        self.buttonlw.setFixedSize(500, 200)
        self.buttonlw.setVisible(False)

# counter button
    def create_button(self):
        self.button = QPushButton('tries : \n 10', self.my_widget)
        self.button.move(670, 20)
        self.button.setFixedSize(100, 100)

# letters buttons
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

# first line
    def createWordLineEdit(self):
        self.word_LineEdit = QLineEdit("", self.my_widget)
        self.word_LineEdit.setFixedSize(600, 40)
        self.word_LineEdit.move(20, 20)
        # self.word_LineEdit.setFont(QFont('NewTimesRoman', 30))
        self.word_LineEdit.setAlignment(Qt.AlignLeft)
        self.word_LineEdit.setPlaceholderText("Enter a word to guess and press 'Enter'...")
        self.word_LineEdit.setReadOnly(False)

# second line
    def createLine(self):
        self.word2_LineEdit = QLineEdit("", self.my_widget)
        self.word2_LineEdit.setFixedSize(600, 40)
        self.word2_LineEdit.move(20, 20)
        self.word2_LineEdit.setAlignment(Qt.AlignLeft)
        self.word2_LineEdit.setReadOnly(True)
        self.word2_LineEdit.setVisible(False)

    def paintEvent(self, event):

        self.painter = QPainter(self)

        # wood base
        if self.counter <= 9:
            self.painter.setPen(QtCore.Qt.black)
            self.painter.setBrush(QtCore.Qt.white)
            self.painter.drawLine(400, 100, 400, 400)

        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.setPen(QtCore.Qt.black)
        self.painter.setBrush(QtCore.Qt.black)

        # wood top
        if self.counter <= 8:
            self.painter.setPen(QtCore.Qt.black)
            self.painter.setBrush(QtCore.Qt.white)
            self.painter.drawLine(200, 100, 400, 100)

        # wood triangle
        if self.counter <= 7:
            self.painter.setPen(QtCore.Qt.black)
            self.painter.setBrush(QtCore.Qt.white)
            self.painter.drawLine(300, 100, 400, 200)

        # rope
        if self.counter <= 6:
            self.painter.setPen(QtCore.Qt.black)
            self.painter.setBrush(QtCore.Qt.white)
            self.painter.drawLine(200, 100, 200, 150)

        # head
        if self.counter <= 5:
            self.painter.setPen(QtCore.Qt.black)
            self.painter.setBrush(QtCore.Qt.white)
            self.painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
            self.painter.drawEllipse(176, 150, 45, 45)

        # body
        if self.counter <= 4:
            self.painter.setPen(QtCore.Qt.black)
            self.painter.setBrush(QtCore.Qt.white)
            self.painter.drawLine(200, 195, 200, 270)

        # left arm
        if self.counter <= 3:
            self.painter.setPen(QtCore.Qt.black)
            self.painter.setBrush(QtCore.Qt.white)
            self.painter.drawLine(200, 195, 170, 220)

        # right arm
        if self.counter <= 2:
            self.painter.setPen(QtCore.Qt.black)
            self.painter.setBrush(QtCore.Qt.white)
            self.painter.drawLine(200, 195, 230, 220)

        # left leg
        if self.counter <= 1:
            self.painter.setPen(QtCore.Qt.black)
            self.painter.setBrush(QtCore.Qt.white)
            self.painter.drawLine(200, 270, 170, 350)

        # right leg
        if self.counter <= 0:
            self.painter.setPen(QtCore.Qt.black)
            self.painter.setBrush(QtCore.Qt.white)
            self.painter.drawLine(200, 270, 230, 350)

        self.painter.end()


class Controler:



    def __init__(self, model, view):
        self.my_model = model

        self.letters = []
        self.list_of_letters = []
        self.string_from_list = ''
        self.guess = ''
        self.j1n = 0
        self.j2n = 0

        self.my_view = view
        self.my_view.word_LineEdit.returnPressed.connect(partial(self.save_new_word))

        view.button1.clicked.connect(lambda: self.button_a())
        view.button1.clicked.connect(lambda: self.my_view.button1.hide())

        view.button2.clicked.connect(lambda: self.button_b())
        view.button2.clicked.connect(lambda: self.my_view.button2.hide())

        view.button3.clicked.connect(lambda: self.button_c())
        view.button3.clicked.connect(lambda: self.my_view.button3.hide())

        view.button4.clicked.connect(lambda: self.button_d())
        view.button4.clicked.connect(lambda: self.my_view.button4.hide())

        view.button5.clicked.connect(lambda: self.button_e())
        view.button5.clicked.connect(lambda: self.my_view.button5.hide())

        view.button6.clicked.connect(lambda: self.button_f())
        view.button6.clicked.connect(lambda: self.my_view.button6.hide())

        view.button7.clicked.connect(lambda: self.button_g())
        view.button7.clicked.connect(lambda: self.my_view.button7.hide())

        view.button8.clicked.connect(lambda: self.button_h())
        view.button8.clicked.connect(lambda: self.my_view.button8.hide())

        view.button9.clicked.connect(lambda: self.button_i())
        view.button9.clicked.connect(lambda: self.my_view.button9.hide())

        view.button10.clicked.connect(lambda: self.button_j())
        view.button10.clicked.connect(lambda: self.my_view.button10.hide())

        view.button11.clicked.connect(lambda: self.button_k())
        view.button11.clicked.connect(lambda: self.my_view.button11.hide())

        view.button12.clicked.connect(lambda: self.button_l())
        view.button12.clicked.connect(lambda: self.my_view.button12.hide())

        view.button13.clicked.connect(lambda: self.button_m())
        view.button13.clicked.connect(lambda: self.my_view.button13.hide())

        view.button14.clicked.connect(lambda: self.button_n())
        view.button14.clicked.connect(lambda: self.my_view.button14.hide())

        view.button15.clicked.connect(lambda: self.button_o())
        view.button15.clicked.connect(lambda: self.my_view.button15.hide())

        view.button16.clicked.connect(lambda: self.button_p())
        view.button16.clicked.connect(lambda: self.my_view.button16.hide())

        view.button17.clicked.connect(lambda: self.button_q())
        view.button17.clicked.connect(lambda: self.my_view.button17.hide())

        view.button18.clicked.connect(lambda: self.button_r())
        view.button18.clicked.connect(lambda: self.my_view.button18.hide())

        view.button19.clicked.connect(lambda: self.button_s())
        view.button19.clicked.connect(lambda: self.my_view.button19.hide())

        view.button20.clicked.connect(lambda: self.button_t())
        view.button20.clicked.connect(lambda: self.my_view.button20.hide())

        view.button21.clicked.connect(lambda: self.button_u())
        view.button21.clicked.connect(lambda: self.my_view.button21.hide())

        view.button22.clicked.connect(lambda: self.button_v())
        view.button22.clicked.connect(lambda: self.my_view.button22.hide())

        view.button23.clicked.connect(lambda: self.button_w())
        view.button23.clicked.connect(lambda: self.my_view.button23.hide())

        view.button24.clicked.connect(lambda: self.button_x())
        view.button24.clicked.connect(lambda: self.my_view.button24.hide())

        view.button25.clicked.connect(lambda: self.button_y())
        view.button25.clicked.connect(lambda: self.my_view.button25.hide())

        view.button26.clicked.connect(lambda: self.button_z())
        view.button26.clicked.connect(lambda: self.my_view.button26.hide())

        view.button27.clicked.connect(lambda: self.button__())
        view.button27.clicked.connect(lambda: self.my_view.button27.hide())

        view.button28.clicked.connect(lambda: self.button_t_())
        view.button28.clicked.connect(lambda: self.my_view.button28.hide())

        view.buttonno.clicked.connect(lambda: self.button_no())
        view.buttonyes.clicked.connect(lambda: self.button_yes())

    def button_no(self):
        quit()

    def button_yes(self):
        self.rerun()


    def rerun(self):
        self.my_view.buttonno.setVisible(False)
        self.my_view.buttonyes.setVisible(False)
        self.my_view.buttonlw.setVisible(False)
        self.my_view.counter = 10
        self.my_view.button.setText('tries : \n 10')
        self.my_view.button1.show()
        self.my_view.button2.show()
        self.my_view.button3.show()
        self.my_view.button4.show()
        self.my_view.button5.show()
        self.my_view.button6.show()
        self.my_view.button7.show()
        self.my_view.button8.show()
        self.my_view.button9.show()
        self.my_view.button10.show()
        self.my_view.button11.show()
        self.my_view.button12.show()
        self.my_view.button13.show()
        self.my_view.button14.show()
        self.my_view.button15.show()
        self.my_view.button16.show()
        self.my_view.button17.show()
        self.my_view.button18.show()
        self.my_view.button19.show()
        self.my_view.button20.show()
        self.my_view.button21.show()
        self.my_view.button22.show()
        self.my_view.button23.show()
        self.my_view.button24.show()
        self.my_view.button25.show()
        self.my_view.button26.show()
        self.my_view.button27.show()
        self.my_view.button28.show()
        self.my_view.word_LineEdit.setReadOnly(False)
        self.my_view.word_LineEdit.setVisible(True)
        self.my_view.word_LineEdit.setPlaceholderText("Enter a word to guess and press 'Enter'...")
        self.my_view.word2_LineEdit.setReadOnly(True)
        self.my_view.word2_LineEdit.setVisible(False)
        self.letters = []
        self.list_of_letters = []
        self.string_from_list = ''
        self.guess = ''

        self.my_view.my_widget.repaint()




    # function for all buttons
    def button_a(self):
        self.letters.append('a')

        if self.my_model.word.find('a') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('a') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_b(self):
        self.letters.append('b')

        if self.my_model.word.find('b') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('b') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_c(self):
        self.letters.append('c')

        if self.my_model.word.find('c') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('c') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()


            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_d(self):
        self.letters.append('d')

        if self.my_model.word.find('d') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('d') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_e(self):
        self.letters.append('e')

        if self.my_model.word.find('e') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('e') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)


    def button_f(self):
        self.letters.append('f')

        if self.my_model.word.find('f') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('f') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_g(self):
        self.letters.append('g')

        if self.my_model.word.find('g') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('g') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_h(self):
        self.letters.append('h')

        if self.my_model.word.find('h') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('h') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_i(self):
        self.letters.append('i')

        if self.my_model.word.find('i') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('i') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_j(self):
        self.letters.append('j')

        if self.my_model.word.find('j') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('j') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_k(self):
        self.letters.append('k')

        if self.my_model.word.find('k') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('k') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_l(self):
        self.letters.append('l')

        if self.my_model.word.find('l') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('l') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_m(self):
        self.letters.append('m')

        if self.my_model.word.find('m') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('m') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_n(self):
        self.letters.append('n')

        if self.my_model.word.find('n') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('n') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_o(self):
        self.letters.append('o')

        if self.my_model.word.find('o') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('o') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_p(self):
        self.letters.append('p')

        if self.my_model.word.find('p') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('p') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_q(self):
        self.letters.append('q')

        if self.my_model.word.find('q') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('q') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_r(self):
        self.letters.append('r')

        if self.my_model.word.find('r') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('r') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_s(self):
        self.letters.append('s')

        if self.my_model.word.find('s') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('s') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_t(self):
        self.letters.append('t')

        if self.my_model.word.find('t') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('t') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_u(self):
        self.letters.append('u')

        if self.my_model.word.find('u') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('u') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_v(self):
        self.letters.append('v')

        if self.my_model.word.find('v') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('v') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_w(self):
        self.letters.append('w')

        if self.my_model.word.find('w') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('w') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_x(self):
        self.letters.append('x')

        if self.my_model.word.find('x') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('x') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_y(self):
        self.letters.append('y')

        if self.my_model.word.find('y') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('y') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_z(self):
        self.letters.append('z')

        if self.my_model.word.find('z') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('z') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button__(self):
        self.letters.append('-')

        if self.my_model.word.find('-') > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find('-') == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

    def button_t_(self):
        self.letters.append("'")

        if self.my_model.word.find("'") > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find("'") == -1:
            if self.my_view.counter - 1 > -1:
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()

            if self.my_view.counter - 1 < 0:
                self.j1n += 1
                self.my_view.j1.setText(str(self.j1n))
                self.my_view.counter -= 1
                self.button_text()
                self.my_view.my_widget.repaint()
                self.my_view.buttonlw.setText(self.my_model.l)
                self.my_view.buttonlw.setVisible(True)
                self.my_view.buttonno.setVisible(True)
                self.my_view.buttonyes.setVisible(True)

        if self.guess == self.my_model.word:
            self.j2n += 1
            self.my_view.j2.setText(str(self.j2n))
            self.my_view.buttonlw.setText('You won!!!\n New game?')
            self.my_view.buttonlw.setVisible(True)
            self.my_view.buttonno.setVisible(True)
            self.my_view.buttonyes.setVisible(True)

# function for button with counter
    def button_text(self):

        if self.my_view.counter == 9:
            self.my_view.button.setText("9")

        if self.my_view.counter == 8:
            self.my_view.button.setText("8")

        if self.my_view.counter == 7:
            self.my_view.button.setText("7")

        if self.my_view.counter == 6:
            self.my_view.button.setText("6")

        if self.my_view.counter == 5:
            self.my_view.button.setText("5")

        if self.my_view.counter == 4:
            self.my_view.button.setText("4")

        if self.my_view.counter == 3:
            self.my_view.button.setText("3")

        if self.my_view.counter == 2:
            self.my_view.button.setText("2")

        if self.my_view.counter == 1:
            self.my_view.button.setText("1")

        if self.my_view.counter == 0:
            self.my_view.button.setText("0")

    def save_new_word(self):
        self.my_model.set_word(self.my_view.word_LineEdit.text())
        ein_list = ['_' for i in range(len(self.my_model.word))]
        ein_list = ' '.join(ein_list)
        self.my_view.word2_LineEdit.setPlaceholderText(str(ein_list))
        self.my_view.word_LineEdit.setVisible(False)
        self.my_view.word2_LineEdit.setVisible(True)


class Model:
    def __init__(self):
        self.word = "default"
        self.l = 'l'

    def set_word(self, new_word):
        self.word = new_word
        self.l = 'You lost !!! \n The word was ' + self.word + '\n New game?'
        # print('New word to guess {' + self.word + '} has been saved')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    var_view = View()
    var_view.show()
    var_model = Model()
    Controler(model=var_model, view=var_view)
    sys.exit(app.exec_())
