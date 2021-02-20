'''
Developper: Sithum Nimlaka Abeydheera
Date      : 2021.02.14
'''
import sqlite3
import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from PyUI.removetask_ui import Ui_MainWindow
from PySide2.QtWidgets import QMessageBox
from PySide2 import QtGui

class RemoveTask(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.connectMe()
        self.setWindowIcon(QtGui.QIcon('img\logo.png'))
        self.setWindowTitle("Hello! Add New Task To Your List.")
        self.setFixedHeight(388)
        self.setFixedWidth(621)

    def connectMe(self):
        self.removetask.clicked.connect(self.taskRemove)
        self.removetask.setShortcut('Enter')

    def taskRemove(self):
        if self.validate():
            task_id = self.taskid.text()
            self.taskid.clear()
            query = "DELETE FROM todo_data WHERE id = ?;"
            parameters = (task_id)
            db_filename = 'db/todo.db'
            conn = sqlite3.connect(db_filename)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            cursor.fetchall()
            conn.commit()
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('img\logo.png'))
            msg.setWindowTitle("Task Removed!")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Task Removed Successfully!!!")
            x = msg.exec_()
        else:
            msg1 = QMessageBox()
            msg1.setWindowIcon(QtGui.QIcon('img\logo.png'))
            msg1.setWindowTitle("Error!")
            msg1.setIcon(QMessageBox.Warning)
            msg1.setText("Please Check Input Fields Are Filled.")
            x = msg1.exec_()

    def validate(self):
        return len(self.taskid.text()) != 0

if(__name__=='__main__'):
    app = QApplication(sys.argv)
    mainWindow = RemoveTask()
    mainWindow.show()
    sys.exit(app.exec_())