from PyQt5 import QtCore, QtGui, QtWidgets
from User import  User
import MySQLdb   as mysql


class User_change(object):
    def User_show(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  User()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelUserNum = QtWidgets.QLabel(self.centralwidget)
        self.labelUserNum.setObjectName("labelUserNum")
        self.verticalLayout.addWidget(self.labelUserNum)
        self.lineEditUserNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUserNum.setObjectName("lineEditUserNum")
        self.verticalLayout.addWidget(self.lineEditUserNum)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelUserLogin = QtWidgets.QLabel(self.centralwidget)
        self.labelUserLogin.setObjectName("labelUserLogin")
        self.verticalLayout_2.addWidget(self.labelUserLogin)
        self.lineEditUserLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUserLogin.setObjectName("lineEditUserLogin")
        self.verticalLayout_2.addWidget(self.lineEditUserLogin)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelUserPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelUserPassword.setObjectName("labelUserPassword")
        self.verticalLayout_3.addWidget(self.labelUserPassword)
        self.lineEditUserPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUserPassword.setObjectName("lineEditUserPassword")
        self.verticalLayout_3.addWidget(self.lineEditUserPassword)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelUserLoginStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelUserLoginStatus.setObjectName("labelUserLoginStatus")
        self.verticalLayout_5.addWidget(self.labelUserLoginStatus)
        self.lineEditUserLoginStatus = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUserLoginStatus.setObjectName("lineEditUserLoginStatus")
        self.verticalLayout_5.addWidget(self.lineEditUserLoginStatus)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelUserRegisterDate = QtWidgets.QLabel(self.centralwidget)
        self.labelUserRegisterDate.setObjectName("labelUserRegisterDate")
        self.verticalLayout_6.addWidget(self.labelUserRegisterDate)
        self.lineEditUserRegisterDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUserRegisterDate.setObjectName("lineEditUserRegisterDate")
        self.verticalLayout_6.addWidget(self.lineEditUserRegisterDate)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(self.add)
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.btnDelete.clicked.connect(self.dels)
        self.btnChange = QtWidgets.QPushButton(self.centralwidget)
        self.btnChange.setObjectName("btnChange")
        self.btnChange.clicked.connect(self.change)
        self.horizontalLayout.addWidget(self.btnChange)
        self.btnShow = QtWidgets.QPushButton(self.centralwidget)
        self.btnShow.setObjectName("btnShow")
        self.btnShow.clicked.connect(self.User_show)
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
        self.labelUserNum.setText(_translate("MainWindow", "User_Num"))
        self.labelUserLogin.setText(_translate("MainWindow", "User_Login"))
        self.labelUserPassword.setText(_translate("MainWindow", "User_Password"))
        self.labelUserLoginStatus.setText(_translate("MainWindow", "User_LoginStatus"))
        self.labelUserRegisterDate.setText(_translate("MainWindow", "User_RegisterDate"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        self.btnShow.setText(_translate("MainWindow", "Show"))

    def change(self):

        try:
            User_Num = int(self.lineEditUserNum.text())
            User_Login = self.lineEditUserLogin.text()
            User_Password = self.lineEditUserPassword.text()
            User_LoginStatus = self.lineEditUserLoginStatus.text()
            User_RegisterDate =  self.lineEditUserRegisterDate.text()

        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
            cur = db.cursor()
            ch1="""UPDATE User SET User_Login = %s,User_Password = %s,User_LoginStatus = %s,User_RegisterDate = %s WHERE User_Num = %s"""
            ch2=( User_Login,User_Password,User_LoginStatus,User_RegisterDate,int(User_Num))
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            User_Num = int(self.lineEditUserNum.text())
            User_Login = self.lineEditUserLogin.text()
            User_Password = self.lineEditUserPassword.text()
            User_LoginStatus = self.lineEditUserLoginStatus.text()
            User_RegisterDate = self.lineEditUserRegisterDate.text()
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        cur.execute('insert into User values(%s, %s, %s, %s, %s, %s)', \
            (int(User_Num),  User_Login,User_Password,User_LoginStatus,User_RegisterDate,))
        db.commit()

        cur.close()
        db.close()

    def dels(self):

        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        try:
            ids = int(self.lineEditUserNum.text())
        except:
            return
        cur.execute("DELETE FROM User WHERE User_Num = %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = User_change()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
