from PyQt5 import QtCore, QtGui, QtWidgets
from EquipmentFailureAccountingModel import  EquipmentFailureAccountingModel
import MySQLdb   as mysql


class EquipmentFailureAccountingModel_change(object):
    def EquipmentFailureAccountingModel_show(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  EquipmentFailureAccountingModel()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelEquipmentFailureAccountingNum = QtWidgets.QLabel(self.centralwidget)
        self.labelEquipmentFailureAccountingNum.setObjectName("labelEquipmentFailureAccountingNum")
        self.verticalLayout.addWidget(self.labelEquipmentFailureAccountingNum)
        self.lineEditEquipmentFailureAccountingNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEquipmentFailureAccountingNum.setObjectName("lineEditEquipmentFailureAccountingNum")
        self.verticalLayout.addWidget(self.lineEditEquipmentFailureAccountingNum)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelEquipmentFailureAccountingDate = QtWidgets.QLabel(self.centralwidget)
        self.labelEquipmentFailureAccountingDate.setObjectName("labelEquipmentFailureAccountingDate")
        self.verticalLayout_2.addWidget(self.labelEquipmentFailureAccountingDate)
        self.lineEditEquipmentFailureAccountingDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEquipmentFailureAccountingDate.setObjectName("lineEditEquipmentFailureAccountingDate")
        self.verticalLayout_2.addWidget(self.lineEditEquipmentFailureAccountingDate)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelEquipmentFailureAccountingResult = QtWidgets.QLabel(self.centralwidget)
        self.labelEquipmentFailureAccountingResult.setObjectName("labelEquipmentFailureAccountingResult")
        self.verticalLayout_3.addWidget(self.labelEquipmentFailureAccountingResult)
        self.lineEditEquipmentFailureAccountingResult = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEquipmentFailureAccountingResult.setObjectName("lineEditEquipmentFailureAccountingResult")
        self.verticalLayout_3.addWidget(self.lineEditEquipmentFailureAccountingResult)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelEquipmentFailureAccountingCause = QtWidgets.QLabel(self.centralwidget)
        self.labelEquipmentFailureAccountingCause.setObjectName("labelEquipmentFailureAccountingCause")
        self.verticalLayout_4.addWidget(self.labelEquipmentFailureAccountingCause)
        self.lineEditEquipmentFailureAccountingCause = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEquipmentFailureAccountingCause.setObjectName("lineEditEquipmentFailureAccountingCause")
        self.verticalLayout_4.addWidget(self.lineEditEquipmentFailureAccountingCause)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelEquipmentEquipmentNum = QtWidgets.QLabel(self.centralwidget)
        self.labelEquipmentEquipmentNum.setObjectName("labelEquipmentEquipmentNum")
        self.verticalLayout_5.addWidget(self.labelEquipmentEquipmentNum)
        self.lineEditEquipmentEquipmentNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEquipmentEquipmentNum.setObjectName("lineEditEquipmentEquipmentNum")
        self.verticalLayout_5.addWidget(self.lineEditEquipmentEquipmentNum)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelEmployeeEmployeeNum = QtWidgets.QLabel(self.centralwidget)
        self.labelEmployeeEmployeeNum.setObjectName("labelEmployeeEmployeeNum")
        self.verticalLayout_6.addWidget(self.labelEmployeeEmployeeNum)
        self.lineEditEmployeeEmployeeNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmployeeEmployeeNum.setObjectName("lineEditEmployeeEmployeeNum")
        self.verticalLayout_6.addWidget(self.lineEditEmployeeEmployeeNum)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
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
        self.btnShow.clicked.connect(self.EquipmentFailureAccountingModel_show)
        self.horizontalLayout.addWidget(self.btnShow)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelEquipmentFailureAccountingNum.setText(_translate("MainWindow", "EquipmentFailureAccounting_Num"))
        self.labelEquipmentFailureAccountingDate.setText(_translate("MainWindow", "EquipmentFailureAccounting_Date"))
        self.labelEquipmentFailureAccountingResult.setText(_translate("MainWindow", "EquipmentFailureAccounting_Result"))
        self.labelEquipmentFailureAccountingCause.setText(_translate("MainWindow", "EquipmentFailureAccounting_Cause"))
        self.labelEquipmentEquipmentNum.setText(_translate("MainWindow", "Equipment_Equipment_Num"))
        self.labelEmployeeEmployeeNum.setText(_translate("MainWindow", "Employee_Employee_Num"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        self.btnShow.setText(_translate("MainWindow", "Show"))


    def change(self):

        try:
            EquipmentFailureAccounting_Num = int(self.lineEditEquipmentFailureAccountingNum.text())
            EquipmentFailureAccounting_Date = self.lineEditEquipmentFailureAccountingDate.text()
            EquipmentFailureAccounting_Result = self.lineEditEquipmentFailureAccountingResult.text()
            EquipmentFailureAccounting_Cause = self.lineEditEquipmentFailureAccountingCause.text()
            Equipment_Equipment_Num = int(self.lineEditEquipmentEquipmentNum.text())
            Employee_Employee_Num =  int(self.lineEditEmployeeEmployeeNum.text())

        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
            cur = db.cursor()
            ch1="""UPDATE EquipmentFailureAccountingModel SET EquipmentFailureAccounting_Date = %s,EquipmentFailureAccounting_Result = %s,EquipmentFailureAccounting_Cause = %s,Equipment_Equipment_Num = %s,Employee_Employee_Num = %s WHERE EquipmentFailureAccounting_Num = %s"""
            ch2=( EquipmentFailureAccounting_Date,EquipmentFailureAccounting_Result,EquipmentFailureAccounting_Cause,EquipmentFailureAccounting_Date,int(Equipment_Equipment_Num),int(Employee_Employee_Num),int(EquipmentFailureAccounting_Num))
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            EquipmentFailureAccounting_Num = int(self.lineEditEquipmentFailureAccountingNum.text())
            EquipmentFailureAccounting_Date = self.lineEditEquipmentFailureAccountingDate.text()
            EquipmentFailureAccounting_Result = self.lineEditEquipmentFailureAccountingResult.text()
            EquipmentFailureAccounting_Cause = self.lineEditEquipmentFailureAccountingCause.text()
            Equipment_Equipment_Num = int(self.lineEditEquipmentEquipmentNum.text())
            Employee_Employee_Num = int(self.lineEditEmployeeEmployeeNum.text())
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        cur.execute('insert into EquipmentFailureAccountingModel values(%s, %s, %s, %s, %s, %s)', \
            (int(EquipmentFailureAccounting_Num),  EquipmentFailureAccounting_Date,EquipmentFailureAccounting_Result,EquipmentFailureAccounting_Cause, int(Equipment_Equipment_Num),int(Employee_Employee_Num),))
        db.commit()

        cur.close()
        db.close()

    def dels(self):

        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        try:
            ids = int(self.lineEditEquipmentFailureAccountingNum.text())
        except:
            return
        cur.execute("DELETE FROM EquipmentFailureAccountingModel WHERE EquipmentFailureAccounting_Num = %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EquipmentFailureAccountingModel_change()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())