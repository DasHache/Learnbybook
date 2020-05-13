import sys
from functools import partial
from PyQt5.QtCore import Qt
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
        self.createDisplay()
        self.create_buttons()


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

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText('')

class PyCalcCtrl:

    def __init__(self, view):
        self._view = view
        self._connectSignals()


    def _buildExpression(self, sub_exp):
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)
        print(expression)


    def _connectSignals(self):
        self._view.buttons['1'].clicked.connect(partial(self._buildExpression, "1"))
        self._view.buttons['2'].clicked.connect(partial(self._buildExpression, "2"))
        self._view.buttons['+'].clicked.connect(partial(self._buildExpression, "+"))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = PyCalcul()
    view.show()
    PyCalcCtrl(view=view)
    sys.exit(app.exec_())
