# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_editar_portada.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(201, 81)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setWindowIcon(QtGui.QIcon("estilos/dark_icons/window_icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_editar_portada = QtWidgets.QLabel(self.centralwidget)
        self.lbl_editar_portada.setGeometry(QtCore.QRect(19, 10, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lbl_editar_portada.setFont(font)
        self.lbl_editar_portada.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_editar_portada.setObjectName("lbl_editar_portada")
        self.btn_editar_portada = QtWidgets.QPushButton(self.centralwidget)
        self.btn_editar_portada.setGeometry(QtCore.QRect(20, 40, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_editar_portada.setFont(font)
        self.btn_editar_portada.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_editar_portada.setObjectName("btn_editar_portada")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " GESTOR COMICS - Registro"))
        self.lbl_editar_portada.setText(_translate("MainWindow", "Añadir portada:"))
        self.btn_editar_portada.setText(_translate("MainWindow", "Seleccionar imagen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
