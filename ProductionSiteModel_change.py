from PyQt5 import QtCore, QtGui, QtWidgets
from ProductionSiteModel import  ProductionSiteModel
import MySQLdb   as mysql


class ProductionSiteModel_change(object):
    def ProductionSiteModel_show(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  ProductionSiteModel()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 264)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelProductionSiteNum = QtWidgets.QLabel(self.centralwidget)
        self.labelProductionSiteNum.setObjectName("labelProductionSiteNum")
        self.verticalLayout.addWidget(self.labelProductionSiteNum)
        self.lineEditProductionSiteNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditProductionSiteNum.setObjectName("lineEditProductionSiteNum")
        self.verticalLayout.addWidget(self.lineEditProductionSiteNum)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelProductionSiteName = QtWidgets.QLabel(self.centralwidget)
        self.labelProductionSiteName.setObjectName("labelProductionSiteName")
        self.verticalLayout_2.addWidget(self.labelProductionSiteName)
        self.lineEditProductionSiteName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditProductionSiteName.setObjectName("lineEditProductionSiteName")
        self.verticalLayout_2.addWidget(self.lineEditProductionSiteName)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
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
        self.btnShow.clicked.connect(self.ProductionSiteModel_show)
        self.horizontalLayout.addWidget(self.btnShow)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelProductionSiteNum.setText(_translate("MainWindow", "ProductionSite_Num"))
        self.labelProductionSiteName.setText(_translate("MainWindow", "ProductionSite_Name"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        self.btnShow.setText(_translate("MainWindow", "Show"))



    def change(self):

        try:
            ProductionSite_Num = int(self.lineEditProductionSiteNum.text())
            ProductionSite_Name = self.lineEditProductionSiteName.text()
        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
            cur = db.cursor()
            ch1="""UPDATE ProductionSiteModel SET ProductionSite_Name = %s WHERE ProductionSite_Num = %s"""
            ch2=( ProductionSite_Name,int(ProductionSite_Num))
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            ProductionSite_Num = int(self.lineEditProductionSiteNum.text())
            ProductionSite_Name = self.lineEditProductionSiteName.text()
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        cur.execute('insert into ProductionSiteModel values(%s, %s)', \
            (int(ProductionSite_Num),  ProductionSite_Name,))
        db.commit()

        cur.close()
        db.close()

    def dels(self):

        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        cur = db.cursor()
        try:
            ids = int(self.lineEditProductionSiteNum.text())
        except:
            return
        cur.execute("DELETE FROM ProductionSiteModel WHERE ProductionSite_Num = %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ProductionSiteModel_change()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())