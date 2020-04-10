# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_catalogo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 354)
        MainWindow.setWindowIcon(QtGui.QIcon("estilos/dark_icons/window_icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_catalogo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_catalogo.setGeometry(QtCore.QRect(22, 3, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_catalogo.setFont(font)
        self.lbl_catalogo.setObjectName("lbl_catalogo")
        self.txt_catalogo = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_catalogo.setGeometry(QtCore.QRect(22, 34, 621, 267))
        self.txt_catalogo.setAcceptDrops(False)
        self.txt_catalogo.setReadOnly(True)
        self.txt_catalogo.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txt_catalogo.setObjectName("txt_catalogo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " GESTOR COMICS - Catálogo"))
        self.lbl_catalogo.setText(_translate("MainWindow", "Catálogo Comics:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
