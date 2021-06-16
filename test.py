# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from os import getcwd
from os import startfile
from PIL import Image, ImageDraw, ImageFont
import textwrap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(352, 335)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MAX_W_INPUT = QtWidgets.QLineEdit(self.centralwidget)
        self.MAX_W_INPUT.setGeometry(QtCore.QRect(190, 40, 113, 22))
        self.MAX_W_INPUT.setObjectName("MAX_W_INPUT")
        self.max_w_label = QtWidgets.QLabel(self.centralwidget)
        self.max_w_label.setGeometry(QtCore.QRect(130, 40, 60, 21))
        self.max_w_label.setStyleSheet("font: 8pt \"Tin Doghouse\";")
        self.max_w_label.setObjectName("max_w_label")
        self.MAX_H_INPUT = QtWidgets.QLineEdit(self.centralwidget)
        self.MAX_H_INPUT.setGeometry(QtCore.QRect(190, 70, 113, 21))
        self.MAX_H_INPUT.setObjectName("MAX_H_INPUT")
        self.max_h_label = QtWidgets.QLabel(self.centralwidget)
        self.max_h_label.setGeometry(QtCore.QRect(130, 70, 60, 20))
        self.max_h_label.setStyleSheet("font: 8pt \"Tin Doghouse\";")
        self.max_h_label.setObjectName("max_h_label")
        self.TEXT_WRAP_WIDTH = QtWidgets.QLineEdit(self.centralwidget)
        self.TEXT_WRAP_WIDTH.setGeometry(QtCore.QRect(190, 110, 113, 21))
        self.TEXT_WRAP_WIDTH.setObjectName("TEXT_WRAP_WIDTH")
        self.text_wrap_width_label = QtWidgets.QLabel(self.centralwidget)
        self.text_wrap_width_label.setGeometry(QtCore.QRect(70, 110, 121, 21))
        self.text_wrap_width_label.setStyleSheet("font: 8pt \"Tin Doghouse\";")
        self.text_wrap_width_label.setObjectName("text_wrap_width_label")
        self.current_height_label = QtWidgets.QLabel(self.centralwidget)
        self.current_height_label.setGeometry(QtCore.QRect(80, 150, 121, 21))
        self.current_height_label.setStyleSheet("font: 8pt \"Tin Doghouse\";\n"
"\n"
"")
        self.current_height_label.setObjectName("current_height_label")
        self.CURRENT_HEIGHT_INPUT = QtWidgets.QLineEdit(self.centralwidget)
        self.CURRENT_HEIGHT_INPUT.setGeometry(QtCore.QRect(190, 150, 113, 22))
        self.CURRENT_HEIGHT_INPUT.setObjectName("CURRENT_HEIGHT_INPUT")
        self.padding_label = QtWidgets.QLabel(self.centralwidget)
        self.padding_label.setGeometry(QtCore.QRect(120, 190, 61, 21))
        self.padding_label.setStyleSheet("font: 8pt \"Tin Doghouse\";")
        self.padding_label.setObjectName("padding_label")
        self.PADDING_INPUT = QtWidgets.QLineEdit(self.centralwidget)
        self.PADDING_INPUT.setGeometry(QtCore.QRect(190, 190, 113, 22))
        self.PADDING_INPUT.setObjectName("PADDING_INPUT")
        self.text_width_label = QtWidgets.QLabel(self.centralwidget)
        self.text_width_label.setGeometry(QtCore.QRect(100, 230, 91, 21))
        self.text_width_label.setStyleSheet("font: 8pt \"Tin Doghouse\";")
        self.text_width_label.setObjectName("text_width_label")
        self.TEXT_WIDTH_INPUT = QtWidgets.QLineEdit(self.centralwidget)
        self.TEXT_WIDTH_INPUT.setGeometry(QtCore.QRect(190, 230, 113, 22))
        self.TEXT_WIDTH_INPUT.setObjectName("TEXT_WIDTH_INPUT")
        self.test_button = QtWidgets.QPushButton(self.centralwidget)
        self.test_button.setGeometry(QtCore.QRect(210, 270, 93, 28))
        self.test_button.setStyleSheet("font: 57 9pt \"Montserrat Medium\";\n"
"color: rgb(255, 0, 0);")
        self.test_button.setObjectName("test_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("TEST POSITION", "TEST POSITION"))
        self.max_w_label.setText(_translate("MainWindow", "MAX_W : "))
        self.max_h_label.setText(_translate("MainWindow", "MAX_H : "))
        self.text_wrap_width_label.setText(_translate("MainWindow", "TEXT WRAP WIDTH : "))
        self.current_height_label.setText(_translate("MainWindow", "CURRENT HEIGHT :"))
        self.padding_label.setText(_translate("MainWindow", "PADDING :"))
        self.text_width_label.setText(_translate("MainWindow", "TEXT WIDTH :"))
        self.test_button.setText(_translate("MainWindow", "TEST"))
        self.test_button.clicked.connect(self.pass_to_create)
    def pass_to_create(self):
        cc = threading.Thread(target = lambda:create(self))
        cc.start()
        
    
    
def create(self):
    current_directory = getcwd()
    MAX_W = int(self.MAX_W_INPUT.text())
    MAX_H = int(self.MAX_H_INPUT.text())
    TEXT_WRAP_WIDTH = int(self.TEXT_WRAP_WIDTH.text())
    CURRENT_HEIGHT = int(self.CURRENT_HEIGHT_INPUT.text())
    PADDING = int(self.PADDING_INPUT.text())
    TEXT_WIDTH = int(self.TEXT_WIDTH_INPUT.text())
    i = "test name"
    im = Image.open(r'cert.jpg')
    d = ImageDraw.Draw(im)
    astr = i
    text_color = (61, 69, 70)
    para = textwrap.wrap(astr, width=int(TEXT_WRAP_WIDTH))
    font = ImageFont.truetype('AgencyFB-Bold.ttf', TEXT_WIDTH)
    current_h, pad = CURRENT_HEIGHT, PADDING
    for line in para:
        w, h = d.textsize(line, font=font)
        d.text(((MAX_W - w) / 2, current_h), line,fill = text_color, font=font)
        current_h += h + pad
    save_location = current_directory + '/Temp/' + i + ".jpg"
    im.save(save_location, "JPEG")
    startfile(save_location)
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

