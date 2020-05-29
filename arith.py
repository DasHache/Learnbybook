import sys
from functools import partial
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QStatusBar, QToolBar, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtGui import QFont
import operator
from random import randint
import datetime

class View(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Arithmetics')
        self.setGeometry(100, 100, 700, 600)

        self.my_widget = QWidget(self)
        self.setCentralWidget(self.my_widget)

        self.my_layout = QVBoxLayout()
        self.my_widget.setLayout(self.my_layout)

        self.createExpression()
        self.createAnswer()
        self.createResult()
        self.createHistory()
        self.createTime()

    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and source is self.answer):
            print('key press:', (event.key(), event.text()))
        return super(View, self).eventFilter(source, event)

    def createExpression(self):
        self.x = QLineEdit()
        self.x.setFixedHeight(45)
        self.x.setFont(QFont('NewTimesRoman', 30)) 
        self.x.setAlignment(Qt.AlignRight)
        self.x.setPlaceholderText("x OP y ")
        self.x.setReadOnly(True)
        self.my_layout.addWidget(self.x)

    def createAnswer(self):
        self.answer = QLineEdit()
        self.answer.setFixedHeight(45)
        self.answer.setFont(QFont('NewTimesRoman', 30)) 
        self.answer.setAlignment(Qt.AlignLeft)
        self.answer.setPlaceholderText("Enter the result and press Enter or Space")
        self.answer.setReadOnly(False)   
        self.my_layout.addWidget(self.answer)

    def createResult(self):
        self.result = QLineEdit()
        self.result.setFixedHeight(45)
        self.result.setFont(QFont('NewTimesRoman', 30)) 
        self.result.setAlignment(Qt.AlignLeft)
        self.result.setPlaceholderText("result is...")
        self.result.setReadOnly(False)   
        self.my_layout.addWidget(self.result)

    def createHistory(self):
        self.history = QTextEdit()
        self.history.setFixedHeight(300)
        self.history.setFont(QFont('NewTimesRoman', 15)) 
        self.history.setAlignment(Qt.AlignLeft)
        self.history.setReadOnly(False)   
        self.my_layout.addWidget(self.history)

    def createTime(self):
        self.t = QLabel("time passed")
        self.my_layout.addWidget(self.t)


class Controler:

    def __init__(self, model, view):
        self.my_model = model

        self.my_view = view
        self.__update_view()
        self.my_view.answer.returnPressed.connect(partial(self.check_results))
        self.my_view.answer.setFocus()

        self.my_view.answer.textEdited.connect(partial(self.check_edit))
        #self.my_view.answer.installEventFilter(self.my_view)

    def check_edit(self, t):
        if t[-1:] == " ":
            self.check_results()

    def get_op_as_str(self, op):
        if op == operator.truediv:
            return " / "

    def check_results(self):
        self.update()
        self.__update_view()

    def __update_view(self):
        self.my_model.x = randint(1,100)
        self.my_model.y = randint(1,100)
        self.my_model.op = operator.truediv
        self.my_view.x.setText(str(self.my_model.x) + self.get_op_as_str(self.my_model.op) + str(self.my_model.y))

    def update(self):

        answer_s = self.my_view.answer.text()
        answer_f = float(answer_s) if answer_s!="" else 0.0
        result_str = self.my_model.calc(answer_f)
        self.my_view.result.setText(result_str)
        self.my_view.answer.setText("")

        speed = self.my_model.get_speed()
        err = self.my_model.get_avg_error()
        n = self.my_model.get_number()
        self.my_view.t.setText( '[ {} ] Speed: {:03.3f} x/s; Error: {:03.3f} %; Score: {} x/s*%'.format(n, speed, err, int(speed/err*1000)) )

        history_text = self.my_view.history.toPlainText()
        new_line = '\n {} = {:03.3f} <--- {} >> {:03.3f}'.format(self.my_view.x.text(), answer_f, result_str, err)
        self.my_view.history.setText(history_text + new_line)



class Model:
    def __init__(self):
        self.t_start = datetime.datetime.now(datetime.timezone.utc)
        self.x = None
        self.y = None
        self.op = operator.truediv
        self.answer = None
        self.errors = []

    def calc(self, user_answer):
        ret = self.op(self.x, self.y) 
        err = abs(ret - user_answer)/abs(ret)*100
        self.errors.append(err)
        return ( 'Correct: {:03.3f}, Your error: {:03.3f}% '.format(ret, err) )

    def get_avg_error(self):
        return sum(self.errors)/self.get_number() + 1e-9 

    def get_time(self):
        return (datetime.datetime.now(datetime.timezone.utc) - self.t_start).total_seconds()

    def get_number(self):
        return len(self.errors)

    def get_speed(self):
        return self.get_number()/self.get_time()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    var_view = View()
    var_view.show()
    var_model = Model()
    Controler(model=var_model, view=var_view)
    sys.exit(app.exec_())
