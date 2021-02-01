from PyQt5 import QtCore, QtGui, QtWidgets
from EmployeeAccountModel import  EmployeeAccountModel
import MySQLdb   as mysql


class EmployeeAccountModel_change(object):
    def EmployeeAccountModel_show(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  EmployeeAccountModel()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 756)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelEmployeeAccountNum = QtWidgets.QLabel(self.centralwidget)
        self.labelEmployeeAccountNum.setObjectName("labelEmployeeAccountNum")
        self.verticalLayout.addWidget(self.labelEmployeeAccountNum)
        self.lineEditEmployeeAccountNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmployeeAccountNum.setObjectName("lineEditEmployeeAccountNum")
        self.verticalLayout.addWidget(self.lineEditEmployeeAccountNum)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelEmployeeAccountLogin = QtWidgets.QLabel(self.centralwidget)
        self.labelEmployeeAccountLogin.setObjectName("labelEmployeeAccountLogin")
        self.verticalLayout_2.addWidget(self.labelEmployeeAccountLogin)
        self.lineEditEmployeeAccountLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmployeeAccountLogin.setObjectName("lineEditEmployeeAccountLogin")
        self.verticalLayout_2.addWidget(self.lineEditEmployeeAccountLogin)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelEmployeeAccountPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelEmployeeAccountPassword.setObjectName("labelEmployeeAccountPassword")
        self.verticalLayout_3.addWidget(self.labelEmployeeAccountPassword)
        self.lineEditEmployeeAccountPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmployeeAccountPassword.setObjectName("lineEditEmployeeAccountPassword")
        self.verticalLayout_3.addWidget(self.lineEditEmployeeAccountPassword)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelEmployeeAccountLoginStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelEmployeeAccountLoginStatus.setObjectName("labelEmployeeAccountLoginStatus")
        self.verticalLayout_5.addWidget(self.labelEmployeeAccountLoginStatus)
        self.lineEditEmployeeAccountLoginStatus = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmployeeAccountLoginStatus.setObjectName("lineEditEmployeeAccountLoginStatus")
        self.verticalLayout_5.addWidget(self.lineEditEmployeeAccountLoginStatus)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labeEmployeeAccountRegisterDate = QtWidgets.QLabel(self.centralwidget)
        self.labeEmployeeAccountRegisterDate.setObjectName("labeEmployeeAccountRegisterDate")
        self.verticalLayout_6.addWidget(self.labeEmployeeAccountRegisterDate)
        self.lineEditEmployeeAccountRegisterDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmployeeAccountRegisterDate.setObjectName("lineEditEmployeeAccountRegisterDate")
        self.verticalLayout_6.addWidget(self.lineEditEmployeeAccountRegisterDate)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
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
        self.btnShow.clicked.connect(self.EmployeeAccountModel_show)
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
        self.labelEmployeeAccountNum.setText(_translate("MainWindow", "EmployeeAccount_Num"))
        self.labelEmployeeAccountLogin.setText(_translate("MainWindow", "EmployeeAccount_Login"))
        self.labelEmployeeAccountPassword.setText(_translate("MainWindow", "EmployeeAccount_Password"))
        self.labelEmployeeAccountLoginStatus.setText(_translate("MainWindow", "EmployeeAccount_LoginStatus"))
        self.labeEmployeeAccountRegisterDate.setText(_translate("MainWindow", "EmployeeAccount_RegisterDate"))
        self.labelUserUserNum.setText(_translate("MainWindow", "User_User_Num"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        self.btnShow.setText(_translate("MainWindow", "Show"))

    def change(self):

        try:
            EmployeeAccount_Num = int(self.lineEditEmployeeAccountNum.text())
            EmployeeAccount_Login = self.lineEditEmployeeAccountLogin.text()
            EmployeeAccount_Password = self.lineEditEmployeeAccountPassword.text()
            EmployeeAccount_LoginStatus = self.lineEditEmployeeAccountLoginStatus.text()
            EmployeeAccount_RegisterDate =  self.lineEditEmployeeAccountRegisterDate.text()
            User_User_Num = int(self.lineEditUserUserNum.text())

        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
            cur = db.cursor()
            ch1="""UPDATE EmployeeAccountModel SET EmployeeAccount_Login = %s,EmployeeAccount_Password = %s,EmployeeAccount_LoginStatus = %s,EmployeeAccount_RegisterDate = %s,User_User_Num = %s WHERE EmployeeAccount_Num = %s"""
            ch2=( EmployeeAccount_Login,EmployeeAccount_Password,EmployeeAccount_LoginStatus,EmployeeAccount_RegisterDate,int(User_User_Num),int(EmployeeAccount_Num))
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            EmployeeAccount_Num = int(self.lineEditEmployeeAccountNum.text())
            EmployeeAccount_Login = self.lineEditEmployeeAccountLogin.text()
            EmployeeAccount_Password = self.lineEditEmployeeAccountPassword.text()
            EmployeeAccount_LoginStatus = self.lineEditEmployeeAccountLoginStatus.text()
            EmployeeAccount_RegisterDate = self.lineEditEmployeeAccountRegisterDate.text()
            User_User_Num = int(self.lineEditUserUserNum.text())
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        cur.execute('insert into EmployeeAccountModel values(%s, %s, %s, %s, %s, %s)', \
            (int(EmployeeAccount_Num),  EmployeeAccount_Login,EmployeeAccount_Password,EmployeeAccount_LoginStatus,EmployeeAccount_RegisterDate,int(User_User_Num),))
        db.commit()

        cur.close()
        db.close()

    def dels(self):

        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        try:
            ids = int(self.lineEditEmployeeAccountNum.text())
        except:
            return
        cur.execute("DELETE FROM EmployeeAccountModel WHERE EmployeeAccount_Num = %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EmployeeAccountModel_change()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

