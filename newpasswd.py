'''
Developper: Sithum Nimlaka Abeydheera
Date      : 2021.02.14
'''
import sqlite3
import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from PyUI.newpasswd_ui import Ui_MainWindow
from PySide2.QtWidgets import QMessageBox
from PySide2 import QtGui

class PasswordChange(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.connectMe()
        self.setWindowIcon(QtGui.QIcon('img\logo.png'))
        self.setWindowTitle("Hello! Change Your Password in Here.")
        self.setFixedHeight(388)
        self.setFixedWidth(621)

    def connectMe(self):
        self.updatepasswd.clicked.connect(self.updatePasswd)
        self.updatepasswd.setShortcut('Enter')

    def updatePasswd(self):
        if self.validator():
            username = self.username.text()
            update_passwd = self.newpass.text()
            self.username.clear()
            self.newpass.clear()
            query = "UPDATE creds SET password = ? WHERE user = ?"
            parameters = (update_passwd, username)
            db_filename = 'db/todo.db'
            conn = sqlite3.connect(db_filename)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            cursor.fetchall()
            conn.commit()
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('img\logo.png'))
            msg.setWindowTitle("Password Updates")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Password Update Successfully!!!")
            x = msg.exec_()
        else:
            msg1 = QMessageBox()
            msg1.setWindowIcon(QtGui.QIcon('img\logo.png'))
            msg1.setWindowTitle("Password Updates : Error!")
            msg1.setIcon(QMessageBox.Information)
            msg1.setText("Something Went Wrong. Please Check Input Fields Are Filled!")
            x = msg1.exec_()

    def validator(self):
        return len(self.username.text()) != 0 and len(self.newpass.text()) != 0

if(__name__=='__main__'):
    app = QApplication(sys.argv)
    mainWindow = PasswordChange()
    mainWindow.show()
    sys.exit(app.exec_())