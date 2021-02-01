from PyQt5 import QtCore, QtGui, QtWidgets
from Manager import  Manager
import MySQLdb   as mysql


class Manager_change(object):
    def Manager_show(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Manager()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 342)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelManagerNum = QtWidgets.QLabel(self.centralwidget)
        self.labelManagerNum.setObjectName("labelManagerNum")
        self.verticalLayout.addWidget(self.labelManagerNum)
        self.lineEditManagerNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditManagerNum.setObjectName("lineEditManagerNum")
        self.verticalLayout.addWidget(self.lineEditManagerNum)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelManagerName = QtWidgets.QLabel(self.centralwidget)
        self.labelManagerName.setObjectName("labelManagerName")
        self.verticalLayout_2.addWidget(self.labelManagerName)
        self.lineEditManagerName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditManagerName.setObjectName("lineEditManagerName")
        self.verticalLayout_2.addWidget(self.lineEditManagerName)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelUserUserNum = QtWidgets.QLabel(self.centralwidget)
        self.labelUserUserNum.setObjectName("labelUserUserNum")
        self.verticalLayout_7.addWidget(self.labelUserUserNum)
        self.lineEditUserUserNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUserUserNum.setObjectName("lineEditUserUserNum")
        self.verticalLayout_7.addWidget(self.lineEditUserUserNum)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(self.add)
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setObjectName("btnDelete")
        self.btnDelete.clicked.connect(self.dels)
        self.horizontalLayout.addWidget(self.btnDelete)
        self.btnChange = QtWidgets.QPushButton(self.centralwidget)
        self.btnChange.setObjectName("btnChange")
        self.btnChange.clicked.connect(self.change)
        self.horizontalLayout.addWidget(self.btnChange)
        self.btnShow = QtWidgets.QPushButton(self.centralwidget)
        self.btnShow.setObjectName("btnShow")
        self.btnShow.clicked.connect(self.Manager_show)
        self.horizontalLayout.addWidget(self.btnShow)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelManagerNum.setText(_translate("MainWindow", "Manager_Num"))
        self.labelManagerName.setText(_translate("MainWindow", "Manager_Name"))
        self.labelUserUserNum.setText(_translate("MainWindow", "User_User_Num"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        self.btnShow.setText(_translate("MainWindow", "Show"))

    def change(self):

        try:
            Manager_Num = int(self.lineEditManagerNum.text())
            Manager_Name = self.lineEditManagerName.text()
            User_User_Num = int(self.lineEditUserUserNum.text())

        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
            cur = db.cursor()
            ch1="""UPDATE Manager SET Manager_Name = %s,User_User_Num = %s WHERE Manager_Num = %s"""
            ch2=(Manager_Name,int(User_User_Num),int(Manager_Num))
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            Manager_Num = int(self.lineEditManagerNum.text())
            Manager_Name = self.lineEditManagerName.text()
            User_User_Num = int(self.lineEditUserUserNum.text())
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        cur.execute('insert into Manager values(%s, %s, %s)', \
            (int(Manager_Num),  Manager_Name,int(User_User_Num),))
        db.commit()

        cur.close()
        db.close()

    def dels(self):

        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        try:
            ids = int(self.lineEditManagerNum.text())
        except:
            return
        cur.execute("DELETE FROM Manager WHERE Manager_Num = %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Manager_change()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())