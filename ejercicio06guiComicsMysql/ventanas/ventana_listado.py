# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_listado.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 354)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setWindowIcon(QtGui.QIcon("estilos/dark_icons/window_icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_listado = QtWidgets.QLabel(self.centralwidget)
        self.lbl_listado.setGeometry(QtCore.QRect(22, 3, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_listado.setFont(font)
        self.lbl_listado.setObjectName("lbl_listado")
        self.lst_listado = QtWidgets.QListWidget(self.centralwidget)
        self.lst_listado.setGeometry(QtCore.QRect(22, 34, 621, 298))
        self.lst_listado.setMinimumSize(QtCore.QSize(0, 251))
        self.lst_listado.setAlternatingRowColors(True)
        self.lst_listado.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lst_listado.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lst_listado.setObjectName("lst_listado")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " GESTOR COMICS - Listado"))
        self.lbl_listado.setText(_translate("MainWindow", "Listado Comics:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
