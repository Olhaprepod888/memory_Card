from PyQt5.QtWidgets import*




# 4 horizontal lines for al widgets:
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()


#таймер - перекур--------------
b_sleep = QPushButton('Відпочити')
timer = QSpinBox()
timer.setValue(30)
#------------------------------


##############ВІКНО З ПИТАННЯМ ###################
#-----box1-----------
#група для варінтів відповідей і направляючих ліній
box1 = QGroupBox('Варіанти відповідей:')

#група для об'єдання варіантів відповідей в єдину систему,
#щоб можна було відповісти тільки на один радіобатон
radio_buttons = QButtonGroup()

rb1 = QRadioButton('')
rb2 = QRadioButton('')
rb3 = QRadioButton('')
rb4 = QRadioButton('')

radio_buttons.addButton(rb1)
radio_buttons.addButton(rb2)
radio_buttons.addButton(rb3)
radio_buttons.addButton(rb4)

v1 = QVBoxLayout()
v2 = QVBoxLayout()

v1.addWidget(rb1, alignment= Qt.AlignCenter)
v1.addWidget(rb2, alignment= Qt.AlignCenter)

v2.addWidget(rb3, alignment= Qt.AlignCenter)
v2.addWidget(rb4, alignment= Qt.AlignCenter)

horizontal= QHBoxLayout()

horizontal.addLayout(v1)
horizontal.addLayout(v2)

box.setLayout(horizontal)#layout add to box(NOT WINDOW!)

#---btn ok----
btn_ok = QPushButton('Відповісти')
h4.addWidget(btn_ok, stretch = 2)

############## ВІКНО З РЕЗУЛЬТАТОМ ###################

#-----------box2------------------
box2 = QGroupBox('Результат теста')

la_1 = QLabel('')#right/not right
la_2 = QLabel('')# correct answer

vertical = QVBoxLayout()
vertical.addWidget(la_1 , alignment = (Qt.AlignLeft| Qt.AlignTop))
vertical.addWidget(la_2 , alignment = Qt.AlignCenter, stretch = 2)

box2.setLayout(vertical)#add layout to box
box2.hide()# hide box with answer





