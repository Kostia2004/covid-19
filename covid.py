# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'covid19.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QLabel)
from PySide2.QtCore import QRect
import COVID19Py
from Сountryes import CountryCode

covid19 = COVID19Py.COVID19()

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        #Form.setStyleSheet(u"background-color: rgb(0, 0, 83)")
        # Create widgets
        self.edit = QLineEdit("Мир")
        self.edit.setObjectName(u"lineEdit")
        self.edit.setGeometry(QRect(20, 20, 361, 31))
        self.edit.setStyleSheet(u"color: #bbbbdb;\n"
"background-color:  rgb(0, 0, 100)")
        
        self.button = QPushButton("Показать")
        self.button.setObjectName(u"pushButton")
        self.button.setGeometry(QRect(40, 80, 321, 41))
        self.button.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 150, 0, 255), stop:1 rgba(255, 255, 0, 205));\n"
"border-radius: 12px;\n"
"color: rgb(75, 48, 1);\n"
"font-size: 20px;")
        
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        var = 73
        if self.edit.text().capitalize()!='Мир':
            code = CountryCode.get(self.edit.text().capitalize(), var)
            if code==var:
                final_message = "Извините, страна не найдена("
            else:
                location = covid19.getLocationByCountryCode(code)
                date = location[0]['last_updated'].split("T")
                time = date[1].split(".")
                final_message = str(self.edit.text()).capitalize()+"\nДанные по стране: \n\tНаселение:" +str(location[0]['country_population'])+"\nПоследнее обновление:"+str(date[0])+" "+str(time[0])+"\n"+"Последние данные:\n"+"\tЗаболевших: "+str(location[0]['latest']['confirmed'])+"\n\t"+"Сметрей: "+str(location[0]['latest']['deaths'])
        else:
            final_message = "Данные по всему миру: \n \t Заболевших: "+str(covid19.getLatest()['confirmed'])+"\n \t Сметрей: "+str(covid19.getLatest()['deaths'])
        self.label = QLabel(final_message)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 140, 361, 91))
        self.label.setStyleSheet(u"backgraund-color: black;\n"
"color: #000000;")
        self.label.show()
        return final_message
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
    #print(Form.greetings)
self.label = QLabel(Form)
