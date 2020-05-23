import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QStatusBar, QToolBar, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout


class View(QMainWindow):
    pass


class Controler:
    def __init__(self, model, view):
        pass


class Model:
    def __init__(self):
        self.word = "abracadabra"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    var_view = View()
    var_view.show()
    model = Model()
    Controler(model=model, view=var_view)
    sys.exit(app.exec_())
