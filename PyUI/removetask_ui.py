# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'removetask_ui.ui'
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
        self.label.setGeometry(QRect(80, 20, 451, 47))
        font = QFont()
        font.setFamily(u"Playball")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(1, 164, 181);\n"
"background-color: transparent;")
        self.removetask = QPushButton(self.centralwidget)
        self.removetask.setObjectName(u"removetask")
        self.removetask.setGeometry(QRect(250, 250, 112, 31))
        font1 = QFont()
        font1.setFamily(u"MV Boli")
        font1.setPointSize(10)
        self.removetask.setFont(font1)
        self.removetask.setCursor(QCursor(Qt.PointingHandCursor))
        self.removetask.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.taskid = QLineEdit(self.centralwidget)
        self.taskid.setObjectName(u"taskid")
        self.taskid.setGeometry(QRect(230, 180, 151, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.taskid.setFont(font2)
        self.taskid.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.taskid.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 130, 133, 26))
        font3 = QFont()
        font3.setFamily(u"MV Boli")
        font3.setPointSize(12)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(1, 164, 181);\n"
"background-color: transparent;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Remove Task From ToDo-List", None))
        self.removetask.setText(QCoreApplication.translate("MainWindow", u"Remove Task", None))
        self.taskid.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter Task Id", None))
    # retranslateUi

