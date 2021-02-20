# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginwindow_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1169, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(254, 138, 139);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(450, 20, 305, 47))
        font = QFont()
        font.setFamily(u"Playball")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(1, 164, 181);\n"
"background-color: transparent;")
        self.user = QLineEdit(self.centralwidget)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(430, 190, 341, 30))
        font1 = QFont()
        font1.setFamily(u"MV Boli")
        font1.setPointSize(12)
        self.user.setFont(font1)
        self.user.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.user.setAlignment(Qt.AlignCenter)
        self.passwd = QLineEdit(self.centralwidget)
        self.passwd.setObjectName(u"passwd")
        self.passwd.setGeometry(QRect(430, 290, 341, 30))
        self.passwd.setFont(font1)
        self.passwd.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.passwd.setEchoMode(QLineEdit.Password)
        self.passwd.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(550, 150, 101, 28))
        font2 = QFont()
        font2.setPointSize(14)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(1, 164, 181);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(550, 250, 95, 28))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(1, 164, 181);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(530, 510, 135, 22))
        font3 = QFont()
        font3.setPointSize(11)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(1, 164, 181);")
        self.loginbtn = QPushButton(self.centralwidget)
        self.loginbtn.setObjectName(u"loginbtn")
        self.loginbtn.setGeometry(QRect(550, 360, 101, 28))
        font4 = QFont()
        font4.setPointSize(10)
        self.loginbtn.setFont(font4)
        self.loginbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginbtn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login To ToDo-List", None))
        self.user.setText("")
        self.passwd.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.loginbtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

