from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton
from PyQt5.QtCore import Qt


app = QApplication([])


lbl_title = QLabel("Профориентационный тест\n\n"
                   "Вам предстоит ответить на 20 вопросов, связанных с различными профессиями\n"
                   "В каждом из них вы должны выбрать наиболее подходящий вам вариант\n"
                   "Чтобы приступить  тесту, нажмите 'Начать'\n")
rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
btn_ok = QPushButton("Начать")

rbtn_1.hide()
rbtn_2.hide()


l_main = QVBoxLayout()

l_h1 = QHBoxLayout()
l_h2 = QHBoxLayout()

l_main.addLayout(l_h1)
l_main.addLayout(l_h2)


def click():
    pass




window  = QWidget()
window.resize(700, 400)
window.setWindowTitle("Профориентационный тест")

window.setLayout(l_main)
window.show()
app.exec_()
