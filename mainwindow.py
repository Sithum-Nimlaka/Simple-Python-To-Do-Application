'''
Developper: Sithum Nimlaka Abeydheera
Date      : 2021.02.14
'''
import sqlite3
import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow, QApplication
from PyUI.mainwindow_ui import Ui_MainWindow
from newpasswd import PasswordChange
from newtask import NewTask
from removetask import RemoveTask
from PySide2 import QtGui


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.connectMe()
        self.setWindowIcon(QtGui.QIcon('img\logo.png'))
        self.setWindowTitle("Welcome! Now You Can Manage Your Tasks.")
        self.setFixedHeight(600)
        self.setFixedWidth(1169)
        self.tableWidget.setColumnWidth(0,10)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,300)
        self.tableWidget.setColumnWidth(4,562)
        self.loadData()
    
    def connectMe(self):
        self.changepasswd_btn.clicked.connect(self.changePasswdBtn)
        self.newtask_btn.clicked.connect(self.newTaskBtn)
        self.refreshbtn.clicked.connect(self.refresh)
        self.deletetask_btn.clicked.connect(self.remTask)

    def loadData(self):
        db_filename = 'db/todo.db'
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todo_data")
        my_result = cursor.fetchall()
        row = 0
        self.tableWidget.setRowCount(len(my_result))
        for x in my_result:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[1])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[2])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(x[3])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x[4])))
            row=row + 1

    def changePasswdBtn(self):
        self.w = PasswordChange()
        self.w.show()

    def newTaskBtn(self):
        self.x = NewTask()
        self.x.show()

    def refresh(self):
        self.hide()
        self.n = MainWindow()
        self.n.show()

    def remTask(self):
        self.s = RemoveTask()
        self.s.show()

if(__name__=='__main__'):
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())