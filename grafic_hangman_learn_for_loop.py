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

        self.buttons = dict() # { "a": buttona, "b": buttonb, .....}
        x = 20
        print("Creating all the buttons......")
        self.button_letters = [chr(x) for x in range(97,120)]
        for letter in self.button_letters:
            button = QPushButton(letter, self.my_widget)
            button.move(x, 500)
            button.setFixedSize(50, 50)
            x = x + 60
            self.buttons[letter] = button



# first line
    def createWordLineEdit(self):
        self.word_LineEdit = QLineEdit("", self.my_widget)
        self.word_LineEdit.setFixedSize(600, 40)
        self.word_LineEdit.move(20, 20)
        # self.word_LineEdit.setFont(QFont('NewTimesRoman', 30))
        self.word_LineEdit.setAlignment(Qt.AlignLeft)
        self.word_LineEdit.setPlaceholderText("The word shall only contain latin letters (- ' accepted), press Enter after entering it.")
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

        print("Connecting all the buttons......")
        print(view.buttons)
        for letter in  view.button_letters:
            bu = view.buttons[letter]
            bu.clicked.connect(lambda: self.func_button(letter))
     

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

        for letter in  ["a", "b", "c", "d"]:
            b = self.my_view.buttons[letter]
            b.show()

        self.my_view.word_LineEdit.clear()
        self.my_view.word_LineEdit.setReadOnly(False)
        self.my_view.word_LineEdit.setVisible(True)
        self.my_view.word_LineEdit.setPlaceholderText("The word shall only contain latin letters (- ' accepted), press Enter after entering it.")
        self.my_view.word2_LineEdit.setReadOnly(True)
        self.my_view.word2_LineEdit.setVisible(False)
        self.letters = []
        self.list_of_letters = []
        self.string_from_list = ''
        self.guess = ''

        self.my_view.my_widget.repaint()




    # function for all buttons
    def func_button(self, letter):
        self.letters.append(letter)

        if self.my_model.word.find(letter) > -1:
            self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                               range(len(self.my_model.word))]
            self.string_from_list = ' '.join(self.list_of_letters)
            self.my_view.word2_LineEdit.setPlaceholderText(str(self.string_from_list.upper()))

        self.list_of_letters = ['_' if self.my_model.word[i] not in self.letters else self.my_model.word[i] for i in
                           range(len(self.my_model.word))]
        self.guess = ''.join(self.list_of_letters)

        if self.my_model.word.find(letter) == -1:
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
