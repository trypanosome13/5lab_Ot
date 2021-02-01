from PyQt5 import QtCore, QtGui, QtWidgets
from Employee import  Employee
import MySQLdb   as mysql


class Employee_change(object):
    def Employee_show(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Employee()
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
        self.labelEmployeeNum = QtWidgets.QLabel(self.centralwidget)
        self.labelEmployeeNum.setObjectName("labelEmployeeNum")
        self.verticalLayout.addWidget(self.labelEmployeeNum)
        self.lineEditEmployeeNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmployeeNum.setObjectName("lineEditEmployeeNum")
        self.verticalLayout.addWidget(self.lineEditEmployeeNum)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelEmployeeName = QtWidgets.QLabel(self.centralwidget)
        self.labelEmployeeName.setObjectName("labelEmployeeName")
        self.verticalLayout_2.addWidget(self.labelEmployeeName)
        self.lineEditEmployeeName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmployeeName.setObjectName("lineEditEmployeeName")
        self.verticalLayout_2.addWidget(self.lineEditEmployeeName)
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
        self.btnShow.clicked.connect(self.Employee_show)
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
        self.labelEmployeeNum.setText(_translate("MainWindow", "Employee_Num"))
        self.labelEmployeeName.setText(_translate("MainWindow", "Employee_Name"))
        self.labelUserUserNum.setText(_translate("MainWindow", "User_User_Num"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        self.btnShow.setText(_translate("MainWindow", "Show"))

    def change(self):

        try:
            Employee_Num = int(self.lineEditEmployeeNum.text())
            Employee_Name = self.lineEditEmployeeName.text()
            User_User_Num = int(self.lineEditUserUserNum.text())

        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
            cur = db.cursor()
            ch1="""UPDATE Employee SET Employee_Name = %s,User_User_Num = %s WHERE Employee_Num = %s"""
            ch2=( Employee_Name,int(User_User_Num),int(Employee_Num))
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            Employee_Num = int(self.lineEditEmployeeNum.text())
            Employee_Name = self.lineEditEmployeeName.text()
            User_User_Num = int(self.lineEditUserUserNum.text())
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        cur.execute('insert into Employee values(%s, %s, %s)', \
            (int(Employee_Num),  Employee_Name,int(User_User_Num),))
        db.commit()

        cur.close()
        db.close()

    def dels(self):

        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        try:
            ids = int(self.lineEditEmployeeNum.text())
        except:
            return
        cur.execute("DELETE FROM Employee WHERE Employee_Num = %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Employee_change()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
