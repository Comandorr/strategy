from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer

app = QApplication([])

timer = QTimer()

lbl_title = QLabel("Тест Руфье\n")

lbl_fio = QLabel("ФИО")
lbl_age = QLabel("Возраст")

edt_fio = QLineEdit()
edt_age = QLineEdit()

lbl_pulse1 = QLabel("пульс 1")
lbl_pulse2 = QLabel("пульс 2")
lbl_pulse3 = QLabel("пульс 3")

edt_pulse1 = QLineEdit()
edt_pulse2 = QLineEdit()
edt_pulse3 = QLineEdit()

edt_help = QTextEdit()
edt_help.setText("ИНСТРУКЦИЯ\n\nЧтобы приступить к тесту, нажмите 'начать'")
lbl_timer = QLabel("--:--")
btn_ok = QPushButton("Начать")


l_main = QVBoxLayout()
l_h_top = QHBoxLayout()
l_h_bot = QHBoxLayout()

l_h_top.addWidget(lbl_fio)
l_h_top.addWidget(edt_fio)
l_h_top.addWidget(lbl_age)
l_h_top.addWidget(edt_age)

l_v1 = QVBoxLayout()
l_v2 = QVBoxLayout()

l_h1 = QHBoxLayout()
l_h2 = QHBoxLayout()
l_h3 = QHBoxLayout()

l_h1.addWidget(lbl_pulse1)
l_h2.addWidget(lbl_pulse2)
l_h3.addWidget(lbl_pulse3)
l_h1.addWidget(edt_pulse1, alignment=Qt.AlignCenter)
l_h2.addWidget(edt_pulse2, alignment=Qt.AlignCenter)
l_h3.addWidget(edt_pulse3, alignment=Qt.AlignCenter)

l_h_right = QHBoxLayout()
l_h_right.addWidget(lbl_timer, alignment=Qt.AlignCenter)
l_h_right.addWidget(btn_ok)

l_v1.addLayout(l_h1)
l_v1.addLayout(l_h2)
l_v1.addLayout(l_h3)

l_v2.addWidget(edt_help)
l_v2.addLayout(l_h_right)

l_h_bot.addLayout(l_v1)
l_h_bot.addLayout(l_v2)

l_main.addWidget(lbl_title, alignment=Qt.AlignCenter)
l_main.addLayout(l_h_top)
l_stels = QHBoxLayout()
l_stels.addWidget(QLabel("\n"))
l_main.addLayout(l_stels)
l_main.addLayout(l_h_bot)

t=10
def tick():
    global t
    if t>=0:
        if t >=10:
            lbl_timer.setText("00:"+str(t))
        else:
            lbl_timer.setText("00:0"+str(t))
        t-=1
    if t<0:
        lbl_timer.setText("время вышло")
        edt_help.setText("ИНСТРУКЦИЯ\n"
                         + "\nЛожитесь и замерьте пульс за первые 15 секунд"
                         + "\nСпустя 30 секунд после первого измерения измерьте его еще за 15 секунд"
                         + "\nВпишите результаты в поля 2 и 3"
                         + "\nПосле нажмите 'Продолжить', чтобы рассчитать результат"
                         )
        timer.stop()


stage = 0
def click():
    global t, stage
    try:
        if stage == 0: # начало первого измерения
            edt_help.setText("ИНСТРУКЦИЯ\n"
                             + "\nЛожитесь и отдыхайте в течение 5 минут"
                             + "\nПо прошествии этого времени посчитайте свой пульс за 15 секунд и впишите его поле 1"
                             + "\nКак будете готовы, нажмите 'Продолжить'"
                             )
            btn_ok.setText("Продолжить")

        elif stage == 1: # инструкция перед приседаниями
            edt_help.setText("ИНСТРУКЦИЯ\n"
                             + "\nСейчас вам предстоит выполнить 30 приседаний за 45 секунд"
                             + "\nТаймер ниже будет отсчитывать время"
                             + "\nПеред тем как начать, заполните поле 'возраст'"
                             + "\nНажмите 'Продолжить', как будете готовы приступить"
                             )
            p1 = int(edt_pulse1.text())
            if p1 <= 0: 1/0

        elif stage == 2: # после приседаний

            timer.timeout.connect(tick)
            timer.start(1000)

            age = int(edt_age.text())
            if age <= 0: 1/0

        elif stage >= 3 and t < 0: # финал
            lbl_timer.setText("--:--")
            p1 = int(edt_pulse1.text())
            p2 = int(edt_pulse2.text())
            p3 = int(edt_pulse3.text())
            age = int(edt_age.text())
            if p1 <= 0 or p2 <= 0: 1/0
            index = ((4 * (p1 + p2 + p3)) - 200)/10

            if age >= 15:
                start = 0
            elif 13 <=  age <= 14:
                start = 1.5
            elif 11 <= age <= 12:
                start = 3
            elif 9 <= age <= 10:
                start = 4.5
            elif 7 <= age <= 8:
                start = 6

            diff = index - start

            if diff < 0.5:
                level = "высокий"
            elif 0.5 <= diff <= 5:
                level = "выше среднего"
            elif 5 < diff <= 10:
                level = "средний"
            elif 10 < diff <= 15:
                level = "удовлетворительный"
            elif diff > 15:
                level = "низкий"

            edt_help.setText("Результат\n"
                             + "\nВаш индекс Руфье равен " + str(index)
                             + "\nДля вашего возраста это  уровень '" + level + "'"
                             )

        stage += 1
    except:
            edt_help.setText("ОШИБКА\n"
                             + "\nДанные введены некорректно"
                             + "\nПроверьте их правильность и попробуйте снова")

btn_ok.clicked.connect(click)





window  = QWidget()
window.resize(700, 400)
window.setWindowTitle("Тест Руфье")

window.setLayout(l_main)
window.show()
app.exec_()
