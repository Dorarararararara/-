from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint
app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle("Генератор победителя")
main_win.resize(400, 200)
winner = QLabel("Нажми, чтобы узнать победителя")
winners = QLabel("?")
button = QPushButton("Сгенерировать")

v_line = QVBoxLayout()
v_line.addWidget(winner, alignment=Qt.AlignCenter)
v_line.addWidget(winners, alignment=Qt.AlignCenter)
v_line.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(v_line)

def button_clicked():
    winner.setText("Победитель")
    winners.setText(str(randint(1, 100)))
    button.hide()

button.clicked.connect(button_clicked)

main_win.show()
app.exec_()
