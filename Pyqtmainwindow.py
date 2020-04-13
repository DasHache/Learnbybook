import sys

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar

class Window(QMainWindow):
    # Main window, in the bracket from which class it inherits to become it
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        self.setCentralWidget(QLabel("I'm the Central Widget")) # imperatively need it
        # private methods, create different GUI elements
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self): # main menu called Menu
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close) # closes the app if pressed

    def _createToolBar(self): #  toolbar with a functional Exit tool button
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self): # status bar at the bottom of the window
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())