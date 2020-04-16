# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(231, 227)
        MainWindow.setStyleSheet("* {\n"
"    background-image: url(\"marmol.jpg\");\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_texto = QtWidgets.QLabel(self.centralwidget)
        self.label_texto.setGeometry(QtCore.QRect(20, 0, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.label_texto.setFont(font)
        self.label_texto.setObjectName("label_texto")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(20, 170, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_resultado.setFont(font)
        self.label_resultado.setStyleSheet("* {\n"
"    border-style: inset;\n"
"    border-width:5px;\n"
"    border-color: rgb(170, 170, 255);\n"
"}")
        self.label_resultado.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_resultado.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_resultado.setText("")
        self.label_resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resultado.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_resultado.setObjectName("label_resultado")
        self.entrada_num = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_num.setGeometry(QtCore.QRect(20, 60, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.entrada_num.setFont(font)
        self.entrada_num.setStyleSheet("* {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: inset;\n"
"    border-width: 5px;\n"
"    border-color: rgb(170, 170, 255);\n"
"}")
        self.entrada_num.setFrame(True)
        self.entrada_num.setAlignment(QtCore.Qt.AlignCenter)
        self.entrada_num.setObjectName("entrada_num")
        self.btn_convertir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_convertir.setGeometry(QtCore.QRect(20, 110, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.btn_convertir.setFont(font)
        self.btn_convertir.setStyleSheet("")
        self.btn_convertir.setObjectName("btn_convertir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CONVERSOR"))
        self.label_texto.setText(_translate("MainWindow", "Introduce un nº romano o natural\n"
"menor de 4000:"))
        self.btn_convertir.setText(_translate("MainWindow", "CONVERTIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
