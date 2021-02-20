# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newtask_ui.ui'
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
        self.label.setGeometry(QRect(420, 20, 365, 47))
        font = QFont()
        font.setFamily(u"Playball")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(1, 164, 181);\n"
"background-color: transparent;")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 90, 1111, 381))
        font1 = QFont()
        font1.setPointSize(12)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.date = QLineEdit(self.groupBox)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(300, 90, 221, 30))
        font2 = QFont()
        font2.setFamily(u"MV Boli")
        font2.setPointSize(12)
        self.date.setFont(font2)
        self.date.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.date.setAlignment(Qt.AlignCenter)
        self.time = QLineEdit(self.groupBox)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(590, 90, 221, 30))
        self.time.setFont(font2)
        self.time.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.time.setEchoMode(QLineEdit.Normal)
        self.time.setAlignment(Qt.AlignCenter)
        self.description = QLineEdit(self.groupBox)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(300, 310, 511, 30))
        self.description.setFont(font2)
        self.description.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.description.setAlignment(Qt.AlignCenter)
        self.title = QLineEdit(self.groupBox)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(300, 200, 511, 30))
        self.title.setFont(font2)
        self.title.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.title.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 60, 55, 16))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(670, 60, 55, 16))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(530, 160, 55, 16))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(420, 270, 283, 26))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.addtask = QPushButton(self.centralwidget)
        self.addtask.setObjectName(u"addtask")
        self.addtask.setGeometry(QRect(540, 510, 93, 28))
        font3 = QFont()
        font3.setFamily(u"MV Boli")
        font3.setPointSize(10)
        self.addtask.setFont(font3)
        self.addtask.setCursor(QCursor(Qt.PointingHandCursor))
        self.addtask.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"New Task To ToDo-List", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"New Task", None))
        self.date.setText("")
        self.time.setText("")
        self.description.setText("")
        self.title.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Little Description About Task", None))
        self.addtask.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
    # retranslateUi