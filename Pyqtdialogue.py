import sys

from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QVBoxLayout

#creates a full class Dialog for the GUI, which inherits from QDialog.
class Dialog(QDialog):
    """Dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Job:', QLineEdit())
        formLayout.addRow('Hobbies:', QLineEdit())
        # you’ll notice that layout managers can be nested inside one another
        dlgLayout.addLayout(formLayout)
        # provides a convenient object to place the dialog buttons.
        btns = QDialogButtonBox()
        #  add two standard buttons: Ok and Cancel
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())

# wrap the boilerplate code in an if __name__ == '__main__': idiom. This is considered a best practice for Pythonistas.