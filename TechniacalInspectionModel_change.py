from PyQt5 import QtCore, QtGui, QtWidgets
from TechniacalInspectionModel import  TechniacalInspectionModel
import MySQLdb   as mysql


class TechniacalInspectionModel_change(object):
    def TechniacalInspectionModel_show(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  TechniacalInspectionModel()
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
        self.labelTechniacalInspectionNum = QtWidgets.QLabel(self.centralwidget)
        self.labelTechniacalInspectionNum.setObjectName("labelTechniacalInspectionNum")
        self.verticalLayout.addWidget(self.labelTechniacalInspectionNum)
        self.lineEditTechniacalInspectionNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTechniacalInspectionNum.setObjectName("lineEditTechniacalInspectionNum")
        self.verticalLayout.addWidget(self.lineEditTechniacalInspectionNum)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelTechniacalInspectionDate = QtWidgets.QLabel(self.centralwidget)
        self.labelTechniacalInspectionDate.setObjectName("labelTechniacalInspectionDate")
        self.verticalLayout_2.addWidget(self.labelTechniacalInspectionDate)
        self.lineEditTechniacalInspectionDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTechniacalInspectionDate.setObjectName("lineEditTechniacalInspectionDate")
        self.verticalLayout_2.addWidget(self.lineEditTechniacalInspectionDate)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelTechniacalInspectionResult = QtWidgets.QLabel(self.centralwidget)
        self.labelTechniacalInspectionResult.setObjectName("labelTechniacalInspectionResult")
        self.verticalLayout_3.addWidget(self.labelTechniacalInspectionResult)
        self.lineEditTechniacalInspectionResult = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTechniacalInspectionResult.setObjectName("lineEditTechniacalInspectionResult")
        self.verticalLayout_3.addWidget(self.lineEditTechniacalInspectionResult)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
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
        self.btnShow.clicked.connect(self.TechniacalInspectionModel_show)
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
        self.labelTechniacalInspectionNum.setText(_translate("MainWindow", "TechniacalInspection_Num"))
        self.labelTechniacalInspectionDate.setText(_translate("MainWindow", "TechniacalInspection_Date"))
        self.labelTechniacalInspectionResult.setText(_translate("MainWindow", "TechniacalInspection_Result"))
        self.labelEquipmentEquipmentNum.setText(_translate("MainWindow", "Equipment_Equipment_Num"))
        self.labelEmployeeEmployeeNum.setText(_translate("MainWindow", "Employee_Employee_Num"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        self.btnShow.setText(_translate("MainWindow", "Show"))


    def change(self):

        try:
            TechniacalInspection_Num = int(self.lineEditTechniacalInspectionNum.text())
            TechniacalInspection_Date = self.lineEditTechniacalInspectionDate.text()
            TechniacalInspection_Result = self.lineEditTechniacalInspectionResult.text()
            Equipment_Equipment_Num = int(self.lineEditEquipmentEquipmentNum.text())
            Employee_Employee_Num =  int(self.lineEditEmployeeEmployeeNum.text())

        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
            cur = db.cursor()
            ch1="""UPDATE TechniacalInspectionModel SET TechniacalInspection_Date = %s,TechniacalInspection_Result = %s,Equipment_Equipment_Num = %s,Employee_Employee_Num = %s WHERE TechniacalInspection_Num = %s"""
            ch2=( TechniacalInspection_Date,TechniacalInspection_Result,int(Equipment_Equipment_Num),int(Employee_Employee_Num),int(TechniacalInspection_Num))
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            TechniacalInspection_Num = int(self.lineEditTechniacalInspectionNum.text())
            TechniacalInspection_Date = self.lineEditTechniacalInspectionDate.text()
            TechniacalInspection_Result = self.lineEditTechniacalInspectionResult.text()
            Equipment_Equipment_Num = int(self.lineEditEquipmentEquipmentNum.text())
            Employee_Employee_Num = int(self.lineEditEmployeeEmployeeNum.text())
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        cur.execute('insert into TechniacalInspectionModel values(%s, %s, %s, %s, %s, %s)', \
            (int(TechniacalInspection_Num),  TechniacalInspection_Date,TechniacalInspection_Result,int(Equipment_Equipment_Num),int(Employee_Employee_Num),))
        db.commit()

        cur.close()
        db.close()

    def dels(self):

        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        try:
            ids = int(self.lineEditTechniacalInspectionNum.text())
        except:
            return
        cur.execute("DELETE FROM TechniacalInspectionModel WHERE TechniacalInspection_Num = %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TechniacalInspectionModel_change()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())