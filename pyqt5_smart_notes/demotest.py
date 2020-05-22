import sys
import json
import PyQt5 as pyqt
import PyQt5.QtWidgets as qwidgets
import PyQt5.QtCore as qcore

app = qwidgets.QApplication([])
window = qwidgets.QWidget()
window.resize(600, 400)
window.setWindowTitle("Smart Notes")


button1 = qwidgets.QPushButton("Save")
edit1 = qwidgets.QLineEdit()
text1 = qwidgets.QTextEdit()
button2 = qwidgets.QPushButton("Load")
button3 = qwidgets.QPushButton("New")
list1 = qwidgets.QListWidget()

h1_line = qwidgets.QHBoxLayout()
h1_line.addWidget(edit1)
h1_line.addWidget(button1)
h1_line.addWidget(button2)
h1_line.addWidget(button3)

right_line = qwidgets.QVBoxLayout()
right_line.addLayout(h1_line)
right_line.addWidget(text1)

left_line = qwidgets.QVBoxLayout()
left_line.addWidget(list1)

main_line = qwidgets.QHBoxLayout()
main_line.addLayout(left_line)
main_line.addLayout(right_line)


def save():
    if len(text1.toPlainText()) != 0:
        with open("notes.json", 'r') as file:
            notes = json.load(file)
            body = text1.toPlainText()
            name = edit1.text()
            if edit1.text() == '':
                name = "untitled"
            notes[name] = body
        with open("notes.json", 'w') as file:
            json.dump(notes, file)
        list1.clear()
        for note in notes:
            list1.addItem(note)

    for i in list1.selectedItems():
        i.setSelected(0)

button1.clicked.connect(save)

'''
def load():
    text1.clear()
    edit1.clear()
    with open("notes.json", 'r') as file:
        notes = json.load(file)
        for note in notes:
            text1.setText(text1.toPlainText()+notes[note]+'\n')
            edit1.setText(edit1.text()+note)

button2.clicked.connect(load)
'''

def new():
    save()
    text1.clear()
    edit1.clear()
    for i in list1.selectedItems():
        i.setSelected(0)
button3.clicked.connect(new)


def load2():
    text1.clear()
    edit1.clear()
    item = list1.currentItem().text()
    print(item)
    text1.setText(notes[item])
    edit1.setText(item)

list1.itemSelectionChanged.connect(load2)


with open("notes.json") as r_file:
    if len(r_file.read()) == 0:
        with open("notes.json", 'w') as file:
            json.dump({}, file)
    notes = {}
    data = json.load(r_file)
    for note in notes:
        list1.addItem(note)


window.setLayout(main_line)
window.show()
app.exec_()
