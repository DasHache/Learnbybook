import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget
# QVBoxLayout for boxes

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHBoxLayout')
# already saw
# creates a QHBoxLayout object called layout
layout1 = QHBoxLayout()
# add three buttons to layout with .addWidget(), then the type of the widget is written
layout1.addWidget(QPushButton('Left'))
layout1.addWidget(QPushButton('Center'))
layout1.addWidget(QPushButton('Right'))
# sets layout as your window’s layout with .setLayout().
window.setLayout(layout1)


window.show()

sys.exit(app.exec_())