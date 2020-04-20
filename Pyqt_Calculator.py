import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QStatusBar, QToolBar, Qt, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout

#app = QApplication([])

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
        layout.addWidget(QPushButton('1'), 0, 0)
        layout.addWidget(QPushButton('2'), 0, 1)
        layout.addWidget(QPushButton('3'), 0, 2)
        layout.addWidget(QPushButton('4'), 1, 0)
        layout.addWidget(QPushButton('5'), 1, 1)
        layout.addWidget(QPushButton('6'), 1, 2)
        layout.addWidget(QPushButton('7'), 2, 0)

        # private methods, create different GUI elements
        # self._createMenu()
        # self._createToolBar()
        # self._createStatusBar()

    # def _createMenu(self): # main menu called Menu
       #  self.menu = self.menuBar().addMenu("&Menu")
        # self.menu.addAction('&Exit', self.close) # closes the app if pressed

    # def _createToolBar(self): #  toolbar with a functional Exit tool button
        # tools = QToolBar()
        # self.addToolBar(tools)
        # tools.addAction('Exit', self.close)

   #  def _createStatusBar(self): # status bar at the bottom of the window
        # status = QStatusBar()
        # status.showMessage("I'm the Status Bar")
        # self.setStatusBar(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PyCalcul()
    win.show()
    sys.exit(app.exec_())
