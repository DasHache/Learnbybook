import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
# sys.argv contains the list of command-line arguments passed into a Python script. If your application is not going
# to accept command line arguments, then you can use an empty list instead of sys.argv. That is, you can do something
# like app = QApplication([]). Command line arguments are simply arguments that are specified after the name of the
# program in the system's command line, and these argument values are passed on to your program during program
# execution.

# Graphical User Interfaces. A graphical user interface (GUI) allows a user to interact with a computer program using
# a pointing device
# window = QWidget()
# window.show()  # IMPORTANT!!!!! Windows are hidden by default.

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)
window.show()
# Start the event loop.
# 5. Run your application's event loop (or main loop)
# sys.exit(app.exec_()) allows you to cleanly exit Python and release memory resources when the application terminates.
# app.exec_()
sys.exit(app.exec_())
