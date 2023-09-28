from PyQt5.QtWidgets import QWidget
from memo_card_layout import*

app = QApplication([])
window = QWidget()
w, h = 600, 500
window.resize(w,h)
window.setWindowTitle('Memory Card')
window.move(100,100)


window.setLayout(l_main)
window.show()
app.exec_()

