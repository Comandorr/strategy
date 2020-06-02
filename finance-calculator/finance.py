from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


app = QApplication([])

lbl1 = QLabel("Ставка в процентах")
lbl2 = QLabel("Период начисления")
lbl3 = QLabel("Будущая сумма")
lbl4 = QLabel("Срок достижения суммы")

edt1 = QLineEdit()
edt2 = QLineEdit()
edt3 = QLineEdit()
edt4 = QLineEdit()

lbl_title = QLabel("Финансовый калькулятор")
edt_help = QTextEdit("Заполните все поля и нажмите кнопку 'Рассчитать'")
edt_help.setReadOnly(True)
btn_ok = QPushButton("Рассчитать")


l_main = QVBoxLayout()
l_h = QHBoxLayout()

l_v1 = QVBoxLayout()
l_v2 = QVBoxLayout()

l_h1 = QHBoxLayout()
l_h2 = QHBoxLayout()
l_h3 = QHBoxLayout()
l_h4 = QHBoxLayout()

l_h.addLayout(l_v1)
l_h.addLayout(l_v2)

l_v1.addLayout(l_h1)
l_v1.addLayout(l_h2)
l_v1.addLayout(l_h3)
l_v1.addLayout(l_h4)

l_main.addWidget(lbl_title, alignment=Qt.AlignCenter)
l_main.addLayout(l_h)


l_h1.addWidget(lbl1, alignment=Qt.AlignLeft)
l_h2.addWidget(lbl2, alignment=Qt.AlignLeft)
l_h3.addWidget(lbl3, alignment=Qt.AlignLeft)
l_h4.addWidget(lbl4, alignment=Qt.AlignLeft)

l_h1.addWidget(edt1, alignment=Qt.AlignCenter)
l_h2.addWidget(edt2, alignment=Qt.AlignCenter)
l_h3.addWidget(edt3, alignment=Qt.AlignCenter)
l_h4.addWidget(edt4, alignment=Qt.AlignCenter)

l_v2.addWidget(edt_help)
l_v2.addWidget(btn_ok)



window  = QWidget()
window.resize(800, 600)
window.setWindowTitle("Финансовый калькулятор")

window.setLayout(l_main)
window.show()
app.exec_()
