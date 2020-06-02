from PyQt5.QtWidgets import *
from PyQt5.QtCore import*

app = QApplication([])

lbl1 = QLabel("Ставка в процентах")
lbl2 = QLabel("Периодичность начисления процентов")
lbl3 = QLabel("Будущая сумма")
lbl4 = QLabel("Срок достижения будущей суммы")

edt1 = QLineEdit()
edt2 = QLineEdit()
edt3 = QLineEdit()
edt4 = QLineEdit()

lbl_title = QLabel("Финансовый калькулятор")
edt_help = QTextEdit("Заполните все поля и нажмите кнопку 'Рассчитать'")
btn_ok = QPushButton("Рассчитать")


l_main = QVBoxLayout()
l_h = QHBoxLayout()

l_v1 = QVBoxLayout()
l_v2 = QVBoxLayout()
l_v3 = QVBoxLayout()

l_h.addLayout(l_v1)
l_h.addLayout(l_v2)
l_h.addLayout(l_v3)

l_main.addWidget(lbl_title, alignment=AlignCenter)
l_main.addLayout(l_h)


l_v1.addWidget(lbl1)
l_v1.addWidget(lbl2)
l_v1.addWidget(lbl3)
l_v1.addWidget(lbl4)

l_v2.addWidget(edt1)
l_v2.addWidget(edt2)
l_v2.addWidget(edt3)
l_v2.addWidget(edt4)

l_v3.addWidget(edt_help)
l_v3.addWidget(btn_ok)


window  = QWidget()
window.resize(800, 600)
window.setWindowTitle("Финансовый калькулятор")

window.setLayout(l_main)
window.show()
app.exec_()
