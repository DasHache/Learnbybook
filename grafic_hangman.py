import sys
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QStatusBar, QToolBar, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont


def test_button_clicked():
    print("test_button_clicked")

class View(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Hangman')
        self.setGeometry(100, 100, 500, 400)

        self.my_widget = QWidget(self)
        self.setCentralWidget(self.my_widget)

        self.my_layout = QVBoxLayout()
        self.my_widget.setLayout(self.my_layout)

        self.createWordLineEdit()
        self.create_button()


    def create_button(self):
        self.button = QPushButton()
        self.button.setText("tries")
        self.button.setFixedSize(200, 300)
        self.my_layout.addWidget(self.button)

    def createWordLineEdit(self):
        self.word_LineEdit = QLineEdit()
        self.word_LineEdit.setFixedHeight(45)
        self.word_LineEdit.setFont(QFont('NewTimesRoman', 30)) 
        self.word_LineEdit.setAlignment(Qt.AlignLeft)
        self.word_LineEdit.setPlaceholderText("Enter a word and press 'Enter'...")
        self.word_LineEdit.setReadOnly(False)
        self.my_layout.addWidget(self.word_LineEdit)


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
