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
        MainWindow.resize(231, 221)
        MainWindow.setStyleSheet("* {\n"
"    background-color: rgb(176, 184, 255)\n"
"}") 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_texto = QtWidgets.QLabel(self.centralwidget)
        self.label_texto.setGeometry(QtCore.QRect(20, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.label_texto.setFont(font)
        self.label_texto.setObjectName("label_texto")
        self.boton_convertir_a_dolares = QtWidgets.QToolButton(self.centralwidget)
        self.boton_convertir_a_dolares.setGeometry(QtCore.QRect(20, 100, 51, 51))
        self.boton_convertir_a_dolares.setStyleSheet("* {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.518, y2:0, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius: 25px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("usa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_convertir_a_dolares.setIcon(icon)
        self.boton_convertir_a_dolares.setIconSize(QtCore.QSize(32, 32))
        self.boton_convertir_a_dolares.setObjectName("boton_convertir_a_dolares")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(20, 170, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_resultado.setFont(font)
        self.label_resultado.setStyleSheet("* {\n"
"    border-style: inset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(85, 85, 255);\n"
"    border-radius: 4px;\n"
"}")
        self.label_resultado.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_resultado.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_resultado.setText("")
        self.label_resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resultado.setObjectName("label_resultado")
        self.entrada_euros = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_euros.setGeometry(QtCore.QRect(20, 40, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.entrada_euros.setFont(font)
        self.entrada_euros.setStyleSheet("* {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: inset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(85, 85, 255);\n"
"    border-radius: 4px;\n"
"}")
        self.entrada_euros.setFrame(True)
        self.entrada_euros.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entrada_euros.setObjectName("entrada_euros")
        self.boton_convertir_a_libras = QtWidgets.QToolButton(self.centralwidget)
        self.boton_convertir_a_libras.setGeometry(QtCore.QRect(90, 100, 51, 51))
        self.boton_convertir_a_libras.setStyleSheet("* {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.518, y2:0, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius: 25px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("uk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_convertir_a_libras.setIcon(icon1)
        self.boton_convertir_a_libras.setIconSize(QtCore.QSize(32, 32))
        self.boton_convertir_a_libras.setObjectName("boton_convertir_a_libras")
        self.boton_convertir_a_yuanes = QtWidgets.QToolButton(self.centralwidget)
        self.boton_convertir_a_yuanes.setGeometry(QtCore.QRect(160, 100, 51, 51))
        self.boton_convertir_a_yuanes.setStyleSheet("* {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.518, y2:0, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius: 25px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("china.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_convertir_a_yuanes.setIcon(icon2)
        self.boton_convertir_a_yuanes.setIconSize(QtCore.QSize(32, 32))
        self.boton_convertir_a_yuanes.setObjectName("boton_convertir_a_yuanes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CONVERSOR €"))
        self.label_texto.setText(_translate("MainWindow", "Introduce una cantidad de Euros:"))
        self.boton_convertir_a_dolares.setText(_translate("MainWindow", "D"))
        self.boton_convertir_a_libras.setText(_translate("MainWindow", "L"))
        self.boton_convertir_a_yuanes.setText(_translate("MainWindow", "Y"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
