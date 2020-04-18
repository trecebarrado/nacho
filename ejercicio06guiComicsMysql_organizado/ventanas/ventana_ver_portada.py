# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_ver_portada.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(316, 512)
        MainWindow.setWindowIcon(QtGui.QIcon("estilos/dark_icons/window_icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_img_portada = QtWidgets.QLabel(self.centralwidget)
        self.lbl_img_portada.setGeometry(QtCore.QRect(-1, -1, 318, 470))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.lbl_img_portada.setFont(font)
        self.lbl_img_portada.setStyleSheet("*{font-family: Verdana; font-size: 14px; color: white;}")
        self.lbl_img_portada.setScaledContents(True)
        self.lbl_img_portada.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img_portada.setObjectName("lbl_img_portada")
        self.btn_cambiar_portada = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cambiar_portada.setGeometry(QtCore.QRect(10, 479, 92, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_cambiar_portada.setFont(font)
        self.btn_cambiar_portada.setObjectName("btn_cambiar_portada")
        self.btn_cerrar_portada = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cerrar_portada.setGeometry(QtCore.QRect(214, 479, 92, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_cerrar_portada.setFont(font)
        self.btn_cerrar_portada.setObjectName("btn_cerrar_portada")
        self.btn_borrar_portada = QtWidgets.QPushButton(self.centralwidget)
        self.btn_borrar_portada.setGeometry(QtCore.QRect(112, 479, 92, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_borrar_portada.setFont(font)
        self.btn_borrar_portada.setObjectName("btn_borrar_portada")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_cerrar_portada, self.btn_cambiar_portada)
        MainWindow.setTabOrder(self.btn_cambiar_portada, self.btn_borrar_portada)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GESTOR COMICS"))
        self.lbl_img_portada.setText(_translate("MainWindow", "Sin portada"))
        self.btn_cambiar_portada.setText(_translate("MainWindow", "Cambiar"))
        self.btn_cerrar_portada.setText(_translate("MainWindow", "Aceptar"))
        self.btn_borrar_portada.setText(_translate("MainWindow", "Borrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
