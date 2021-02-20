'''
Developper: Sithum Nimlaka Abeydheera
Date      : 2021.02.14
'''
import sqlite3
import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from PyUI.loginwindow_ui import Ui_MainWindow
from mainwindow import MainWindow
from PySide2.QtWidgets import QMessageBox
from PySide2 import QtGui

class Login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.connectMe()
        self.setWindowIcon(QtGui.QIcon('img\logo.png'))
        self.setWindowTitle("Login To ToDo-List")
        self.setFixedHeight(600)
        self.setFixedWidth(1169)

    def connectMe(self):
        self.loginbtn.clicked.connect(self.userLogin)
        self.loginbtn.setShortcut('Enter')

    def userLogin(self):
        username = self.user.text()
        password = self.passwd.text()
        self.user.clear()
        self.passwd.clear()
        query = "SELECT * FROM creds WHERE user= ? AND password= ?"
        parameters = (username,password)
        db_filename = 'db/todo.db'
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        query_result = cursor.fetchall()
        conn.commit()
        if query_result != []:
            self.hide()
            self.w = MainWindow()
            self.w.show()
        else:
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('img\logo.png'))
            msg.setWindowTitle("Login Error!")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Login Error: Incorrect Username Or Password Entered. Please Try Again.")
            x = msg.exec_()

if(__name__=='__main__'):
    app = QApplication(sys.argv)
    mainWindow = Login()
    mainWindow.show()
    sys.exit(app.exec_())