# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import random

quotes = ['Your limitation—it’s only your imagination.','Push yourself, because no one else is going to do it for you.','Sometimes later becomes never. Do it now.','Great things never come from comfort zones.','Dream it. Wish it. Do it.','Success doesn’t just find you. You have to go out and get it.','The harder you work for something, the greater you’ll feel when you achieve it.','Dream bigger. Do bigger.','Don’t stop when you’re tired. Stop when you’re done.','Wake up with determination. Go to bed with satisfaction.']

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
        self.label.setGeometry(QRect(510, 20, 161, 47))
        font = QFont()
        font.setFamily(u"Playball")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(1, 164, 181);\n"
"background-color: transparent;")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 100, 1111, 311))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.tableWidget.setFont(font1)
        self.tableWidget.setStyleSheet(u"background-color: rgb(1, 164, 181);\n"
"border-radius: 0.5em;")
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.newtask_btn = QPushButton(self.centralwidget)
        self.newtask_btn.setObjectName(u"newtask_btn")
        self.newtask_btn.setGeometry(QRect(320, 480, 161, 51))
        font2 = QFont()
        font2.setFamily(u"MV Boli")
        font2.setPointSize(12)
        self.newtask_btn.setFont(font2)
        self.newtask_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newtask_btn.setStyleSheet(u"background-color: #fdfdff;\n"
"border-radius: 0.5em;")
        self.changepasswd_btn = QPushButton(self.centralwidget)
        self.changepasswd_btn.setObjectName(u"changepasswd_btn")
        self.changepasswd_btn.setGeometry(QRect(30, 480, 161, 51))
        self.changepasswd_btn.setFont(font2)
        self.changepasswd_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.changepasswd_btn.setStyleSheet(u"background-color: #fdfdff;\n"
"border-radius: 0.5em;")
        self.deletetask_btn = QPushButton(self.centralwidget)
        self.deletetask_btn.setObjectName(u"deletetask_btn")
        self.deletetask_btn.setGeometry(QRect(710, 480, 161, 51))
        self.deletetask_btn.setFont(font2)
        self.deletetask_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deletetask_btn.setStyleSheet(u"background-color: #fdfdff;\n"
"border-radius: 0.5em;")
        self.speciallable = QLabel(self.centralwidget)
        self.speciallable.setObjectName(u"speciallable")
        self.speciallable.setGeometry(QRect(20, 550, 1131, 22))
        font3 = QFont()
        font3.setFamily(u"MV Boli")
        font3.setPointSize(9)
        self.speciallable.setFont(font3)
        self.speciallable.setStyleSheet(u"background-color: transparent;")
        self.speciallable.setAlignment(Qt.AlignCenter)
        self.refreshbtn = QPushButton(self.centralwidget)
        self.refreshbtn.setObjectName(u"refreshbtn")
        self.refreshbtn.setGeometry(QRect(980, 480, 161, 51))
        self.refreshbtn.setFont(font2)
        self.refreshbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshbtn.setStyleSheet(u"background-color: #fdfdff;\n"
"border-radius: 0.5em;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ToDo-List", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Discription", None));
        self.newtask_btn.setText(QCoreApplication.translate("MainWindow", u"New Task", None))
        self.changepasswd_btn.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.deletetask_btn.setText(QCoreApplication.translate("MainWindow", u"Delete Task", None))
        self.speciallable.setText(QCoreApplication.translate("MainWindow", u"" + (str(random.choice(quotes))), None))
        self.refreshbtn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
    # retranslateUi

