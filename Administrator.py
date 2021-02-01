from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import MySQLdb as mysql
import ast

def convert(in_data):
    def cvt(data):
        try:
            return ast.literal_eval(data)
        except Exception:
            return str(data)
    return tuple(map(cvt, in_data))


class  Administrator(object):

    def loadconection(self):
        db = mysql.connect(host="localhost", user="root", passwd="trypanosome!3", db="EquipmentFailureAccounting")
        with db:
            cur = db.cursor()
            rows = cur.execute("""select * from Administrator""")
            data = cur.fetchall()

            for row in data:
                self.add_table(convert(row))

            cur.close()

    def add_table(self, columns):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(column)))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(35, 21, 731, 401))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Administrator_Num', 'Administrator_Name', 'User_User_Num'])
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.btnShow = QtWidgets.QPushButton(self.centralwidget)
        self.btnShow.setGeometry(QtCore.QRect(340, 460, 75, 23))
        self.btnShow.setObjectName("btnShow")
        self.btnShow.clicked.connect(self.loadconection)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnShow.setText(_translate("MainWindow", "Show"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui =  Administrator()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())