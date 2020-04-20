# response to event => widget make a signal
# if you want a signal to trigger an action, then you need to connect it to a slot
# can use any Python callable (or callback) as a slot.
# A signal   -> be connected to one or many slots
#            -> connected to another signal
# A slot may be connected to one or many signals

# widget.signal.connect(slot_function)   connects a signal to a slot

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


def greeting():  # future slot
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World!")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
btn.clicked.connect(greeting)  # Connect clicked to greeting()

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())

# Every widget has its own set of predefined signals. You can check them

# for extra arguments

# def greeting(who):
#     """Slot function."""
#     if msg.text():
#         msg.setText('')
#     else:
#         msg.setText(f'Hello {who}')

# if you want to connect it
# btn.clicked.connect(functools.partial(greeting, 'World!'))       need to import functools first
