# the grid layout

import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

# The last layout manager class is QFormLayout, which arranges widgets in a two-column layout. The first column
# usually displays messages in labels. The second column generally contains widgets like QLineEdit, QComboBox,
# QSpinBox, and so on.

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QGridLayout')

layout = QGridLayout()

# the first coordinate is y the second the x
layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)

# if u add rowSpan and columnSpan (4th and 5th arguments) it can expend the button
# the fourth argument can move the button down
# the fifth argument can expend the button but also somehow it can affect other buttons
layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())

# layout.addRow('Name:', QLineEdit())
# layout.addRow('Age:', QLineEdit())
# layout.addRow('Job:', QLineEdit())
# layout.addRow('Hobbies:', QLineEdit())
# method called .addRow(). You can use this method to add a two-widget row to the layout. The first argument of
# .addRow() should be a label, and the second argument should be any other widget that allows the user to enter or
# edit data.
# QLineEdit() gives you the possibility to write something
