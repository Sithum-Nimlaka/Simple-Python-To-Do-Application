'''
Developper: Sithum Nimlaka Abeydheera
Date      : 2021.02.14
'''
import sqlite3
import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from PyUI.newtask_ui import Ui_MainWindow
from PySide2.QtWidgets import QMessageBox
from PySide2 import QtGui


class NewTask(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.connectMe()
        self.setWindowIcon(QtGui.QIcon('img\logo.png'))
        self.setWindowTitle("Hello! Add New Task To Your List.")
        self.setFixedHeight(600)
        self.setFixedWidth(1169)

    def connectMe(self):
        self.addtask.clicked.connect(self.addNewTask)
        self.addtask.setShortcut('Enter')

    def addNewTask(self):
        if self.taskValidator():
            date = self.date.text()
            time = self.time.text()
            title = self.title.text()
            descrip = self.description.text()
            self.date.clear()
            self.time.clear()
            self.title.clear()
            self.description.clear()
            query = "INSERT INTO todo_data(date,time,title,discription) VALUES(?,?,?,?)"
            parameters = (date, time, title, descrip)
            db_filename = 'db/todo.db'
            conn = sqlite3.connect(db_filename)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            cursor.fetchall()
            conn.commit()
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('img\logo.png'))
            msg.setWindowTitle("Task Updates: Success!")
            msg.setIcon(QMessageBox.Information)
            msg.setText("New Task Added Successfully!!!")
            x = msg.exec_()
        else:
            msg1 = QMessageBox()
            msg1.setWindowIcon(QtGui.QIcon('img\logo.png'))
            msg1.setWindowTitle("Task Updates : Error!")
            msg1.setIcon(QMessageBox.Warning)
            msg1.setText("Something Went Wrong! Please Check All Queries are Filled.")
            y = msg1.exec_()

    def taskValidator(self):
        return len(self.date.text()) != 0 and len(self.date.text()) != 0 and len(self.title.text()) != 0 and len(self.description.text()) != 0

if(__name__=='__main__'):
    app = QApplication(sys.argv)
    mainWindow = NewTask()
    mainWindow.show()
    sys.exit(app.exec_())