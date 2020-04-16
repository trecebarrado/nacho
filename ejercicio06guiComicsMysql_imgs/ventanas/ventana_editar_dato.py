# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_editar_dato.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(201, 108)
        MainWindow.setWindowIcon(QtGui.QIcon("estilos/dark_icons/window_icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_editar_dato = QtWidgets.QLabel(self.centralwidget)
        self.lbl_editar_dato.setGeometry(QtCore.QRect(19, 9, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lbl_editar_dato.setFont(font)
        self.lbl_editar_dato.setObjectName("lbl_editar_dato")
        self.txt_editar_dato = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_editar_dato.setGeometry(QtCore.QRect(20, 38, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txt_editar_dato.setFont(font)
        self.txt_editar_dato.setObjectName("txt_editar_dato")
        self.btn_editar_dato = QtWidgets.QPushButton(self.centralwidget)
        self.btn_editar_dato.setGeometry(QtCore.QRect(20, 68, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_editar_dato.setFont(font)
        self.btn_editar_dato.setObjectName("btn_editar_dato")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " GESTOR COMICS - Registro"))
        self.lbl_editar_dato.setText(_translate("MainWindow", "Editar dato:"))
        self.btn_editar_dato.setText(_translate("MainWindow", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
