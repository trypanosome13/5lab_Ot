from PyQt5 import QtCore, QtGui, QtWidgets
from EquipmentModel import  EquipmentModel
import MySQLdb   as mysql


class EquipmentModel_change(object):
    def EquipmentModel_show(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  EquipmentModel()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelEquipmentNum = QtWidgets.QLabel(self.centralwidget)
        self.labelEquipmentNum.setObjectName("labelEquipmentNum")
        self.verticalLayout.addWidget(self.labelEquipmentNum)
        self.lineEditEquipmentNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEquipmentNum.setObjectName("lineEditEquipmentNum")
        self.verticalLayout.addWidget(self.lineEditEquipmentNum)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelEquipmentName = QtWidgets.QLabel(self.centralwidget)
        self.labelEquipmentName.setObjectName("labelEquipmentName")
        self.verticalLayout_2.addWidget(self.labelEquipmentName)
        self.lineEditEquipmentName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEquipmentName.setObjectName("lineEditEquipmentName")
        self.verticalLayout_2.addWidget(self.lineEditEquipmentName)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelProductionSiteProductionSiteNum = QtWidgets.QLabel(self.centralwidget)
        self.labelProductionSiteProductionSiteNum.setObjectName("labelProductionSiteProductionSiteNum")
        self.verticalLayout_3.addWidget(self.labelProductionSiteProductionSiteNum)
        self.lineEditProductionSiteProductionSiteNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditProductionSiteProductionSiteNum.setObjectName("lineEditProductionSiteProductionSiteNum")
        self.verticalLayout_3.addWidget(self.lineEditProductionSiteProductionSiteNum)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
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
        self.btnShow.clicked.connect(self.EquipmentModel_show)
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
        self.labelEquipmentNum.setText(_translate("MainWindow", "Equipment_Num"))
        self.labelEquipmentName.setText(_translate("MainWindow", "Equipment_Name"))
        self.labelProductionSiteProductionSiteNum.setText(_translate("MainWindow", "ProductionSite_ProductionSite_Num"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        self.btnShow.setText(_translate("MainWindow", "Show"))


    def change(self):

        try:
            Equipment_Num = int(self.lineEditEquipmentNum.text())
            Equipment_Name = self.lineEditEquipmentName.text()
            ProductionSite_ProductionSite_Num = int(self.lineEditProductionSiteProductionSiteNum.text())
        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
            cur = db.cursor()
            ch1="""UPDATE EquipmentModel SET Equipment_Name = %s,ProductionSite_ProductionSite_Num = %s WHERE Equipment_Num = %s"""
            ch2=( Equipment_Name,int(ProductionSite_ProductionSite_Num),int(Equipment_Num))
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            Equipment_Num = int(self.lineEditEquipmentNum.text())
            Equipment_Name = self.lineEditEquipmentName.text()
            ProductionSite_ProductionSite_Num = int(self.lineEditProductionSiteProductionSiteNum.text())
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        cur.execute('insert into EquipmentModel values(%s, %s, %s)', \
            (int(Equipment_Num),  Equipment_Name, int(ProductionSite_ProductionSite_Num),))
        db.commit()

        cur.close()
        db.close()

    def dels(self):

        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        try:
            ids = int(self.lineEditEquipmentNum.text())
        except:
            return
        cur.execute("DELETE FROM EquipmentModel WHERE Equipment_Num = %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EquipmentModel_change()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())