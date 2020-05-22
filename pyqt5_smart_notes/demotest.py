import sys
import json
#import PyQt5.QtCore as qcore
import PyQt5.QtWidgets as qwidgets

app = qwidgets.QApplication([])
window = qwidgets.QWidget()
window.resize(600, 400)
window.setWindowTitle("Smart Notes")


button_save = qwidgets.QPushButton("Save")
edit1 = qwidgets.QLineEdit()
text1 = qwidgets.QTextEdit()
button2 = qwidgets.QPushButton("Load")
button_new = qwidgets.QPushButton("New")
list1 = qwidgets.QListWidget()

h1_line = qwidgets.QHBoxLayout()
h1_line.addWidget(edit1)
h1_line.addWidget(button_save)
h1_line.addWidget(button2)
h1_line.addWidget(button_new)

right_line = qwidgets.QVBoxLayout()
right_line.addLayout(h1_line)
right_line.addWidget(text1)

left_line = qwidgets.QVBoxLayout()
left_line.addWidget(list1)

main_line = qwidgets.QHBoxLayout()
main_line.addLayout(left_line)
main_line.addLayout(right_line)

notes = {}


def save():
    global notes
    if len(text1.toPlainText()) != 0:
        body = text1.toPlainText()
        name = edit1.text()
        if not len(edit1.text()):
            name = "untitled"
        notes[name] = body
        with open("notes.json", 'w') as file:
            json.dump(notes, file)
        list1.clear()
        list1.addItems(notes)

    for i in list1.selectedItems():
        i.setSelected(0)

button_save.clicked.connect(save)


def new():
    global notes
    save()
    text1.clear()
    edit1.clear()
    for i in list1.selectedItems():
        i.setSelected(0)

button_new.clicked.connect(new)


def load():
    global notes
    text1.clear()
    edit1.clear()
    item = list1.currentItem().text()
    edit1.setText(item)
    text1.setText(notes[item])

list1.itemSelectionChanged.connect(load)


with open("notes.json", 'r') as file:
    if len(file.read()):
        file.seek(0)
        notes = json.load(file)
    list1.addItems(notes)


window.setLayout(main_line)
window.show()
app.exec_()
