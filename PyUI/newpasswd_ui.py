# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newpasswd_ui.ui'
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
        MainWindow.resize(621, 388)
        MainWindow.setStyleSheet(u"background-color: rgb(254, 138, 139);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 279, 47))
        font = QFont()
        font.setFamily(u"Playball")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(1, 164, 181);\n"
"background-color: transparent;")
        self.updatepasswd = QPushButton(self.centralwidget)
        self.updatepasswd.setObjectName(u"updatepasswd")
        self.updatepasswd.setGeometry(QRect(270, 310, 93, 31))
        font1 = QFont()
        font1.setFamily(u"MV Boli")
        font1.setPointSize(10)
        self.updatepasswd.setFont(font1)
        self.updatepasswd.setCursor(QCursor(Qt.PointingHandCursor))
        self.updatepasswd.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.newpass = QLineEdit(self.centralwidget)
        self.newpass.setObjectName(u"newpass")
        self.newpass.setGeometry(QRect(210, 240, 201, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.newpass.setFont(font2)
        self.newpass.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.newpass.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 190, 201, 26))
        font3 = QFont()
        font3.setFamily(u"MV Boli")
        font3.setPointSize(12)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(1, 164, 181);\n"
"background-color: transparent;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 100, 152, 26))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(1, 164, 181);\n"
"background-color: transparent;")
        self.username = QLineEdit(self.centralwidget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(210, 140, 201, 41))
        self.username.setFont(font2)
        self.username.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.username.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.updatepasswd.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.newpass.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter New Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter Username", None))
        self.username.setText("")
    # retranslateUi

