import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QStatusBar, QToolBar, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout


# app = QApplication([])

# window = QWidget()
# window.setWindowTitle('Calculator')
# window.setGeometry(100, 100, 310, 320)  # x and y  and width and height
# helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
# helloMsg.move(60, 15)
# window.show()

class PyCalcul(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 310, 320)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self.generalLayout = QVBoxLayout()
        self._centralWidget.setLayout(self.generalLayout)
        self.create_buttons()
        self.createDisplay()

    def createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(45)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def create_buttons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                   }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(50, 50)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
            self.generalLayout.addLayout(buttonsLayout)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PyCalcul()
    win.show()
    sys.exit(app.exec_())
