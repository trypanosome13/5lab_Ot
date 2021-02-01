from PyQt5 import QtCore, QtGui, QtWidgets
from EmployeeModel import  EmployeeModel
import MySQLdb   as mysql


class EmployeeModel_change(object):
    def EmployeeModel_show(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  EmployeeModel()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 19, 741, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelEmployee_Num = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelEmployee_Num.setObjectName("labelEmployee_Num")
        self.verticalLayout.addWidget(self.labelEmployee_Num)
        self.lineEditEmployeeNum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditEmployeeNum.setObjectName("lineEditEmployeeNum")
        self.verticalLayout.addWidget(self.lineEditEmployeeNum)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 80, 741, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelEmployeeLastname = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelEmployeeLastname.setObjectName("labelEmployeeLastname")
        self.verticalLayout_2.addWidget(self.labelEmployeeLastname)
        self.lineEditEmployeeLastname = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditEmployeeLastname.setObjectName("lineEditEmployeeLastname")
        self.verticalLayout_2.addWidget(self.lineEditEmployeeLastname)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 140, 741, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelEmployeeFirstname = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelEmployeeFirstname.setObjectName("labelEmployeeFirstname")
        self.verticalLayout_3.addWidget(self.labelEmployeeFirstname)
        self.lineEditEmployee_Firstname = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEditEmployee_Firstname.setObjectName("lineEditEmployee_Firstname")
        self.verticalLayout_3.addWidget(self.lineEditEmployee_Firstname)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 200, 741, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelEmployeePatronumic = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.labelEmployeePatronumic.setObjectName("labelEmployeePatronumic")
        self.verticalLayout_4.addWidget(self.labelEmployeePatronumic)
        self.lineEditEmployeePatronumic = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditEmployeePatronumic.setObjectName("lineEditEmployeePatronumic")
        self.verticalLayout_4.addWidget(self.lineEditEmployeePatronumic)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(30, 260, 741, 51))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelEmployeePosition = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.labelEmployeePosition.setObjectName("labelEmployeePosition")
        self.verticalLayout_5.addWidget(self.labelEmployeePosition)
        self.lineEditEmployee_Position = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEditEmployee_Position.setObjectName("lineEditEmployee_Position")
        self.verticalLayout_5.addWidget(self.lineEditEmployee_Position)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(29, 329, 741, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(self.add)
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnDelete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnDelete.setObjectName("btnDelete")
        self.btnDelete.clicked.connect(self.dels)
        self.horizontalLayout.addWidget(self.btnDelete)
        self.btnChange = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnChange.setObjectName("btnChange")
        self.btnChange.clicked.connect(self.change)
        self.horizontalLayout.addWidget(self.btnChange)
        self.btnShow = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnShow.setObjectName("btnShow")
        self.btnShow.clicked.connect(self.EmployeeModel_show)
        self.horizontalLayout.addWidget(self.btnShow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelEmployee_Num.setText(_translate("MainWindow", "Employee_Num"))
        self.labelEmployeeLastname.setText(_translate("MainWindow", "Employee_Lastname"))
        self.labelEmployeeFirstname.setText(_translate("MainWindow", "Employee_Firstname"))
        self.labelEmployeePatronumic.setText(_translate("MainWindow", "Employee_Patronumic"))
        self.labelEmployeePosition.setText(_translate("MainWindow", "Employee_Position"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        self.btnShow.setText(_translate("MainWindow", "Show"))



    def change(self):

        try:
            Employee_Num = int(self.lineEditEmployeeNum.text())
            Employee_Lastname = self.lineEditEmployeeLastname.text()
            Employee_Firstname = self.lineEditEmployee_Firstname.text()
            Employee_Patronumic = self.lineEditEmployeePatronumic.text()
            Employee_Position = self.lineEditEmployee_Position.text()
        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
            cur = db.cursor()
            ch1="""UPDATE EmployeeModel SET Employee_Lastname = %s,Employee_Firstname = %s, Employee_Patronumic = %s, Employee_Position = %s WHERE Employee_Num = %s"""
            ch2=( Employee_Lastname, Employee_Firstname, Employee_Patronumic, Employee_Position,int(Employee_Num))
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            Employee_Num = int(self.lineEditEmployeeNum.text())
            Employee_Lastname = self.lineEditEmployeeLastname.text()
            Employee_Firstname = self.lineEditEmployee_Firstname.text()
            Employee_Patronumic = self.lineEditEmployeePatronumic.text()
            Employee_Position = self.lineEditEmployee_Position.text()
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        cur.execute('insert into EmployeeModel values(%s, %s, %s, %s, %s)', \
            (int(Employee_Num),  Employee_Lastname, Employee_Firstname, Employee_Patronumic, Employee_Position,))
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
        cur.execute("DELETE FROM EmployeeModel WHERE Employee_Num = %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EmployeeModel_change()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())