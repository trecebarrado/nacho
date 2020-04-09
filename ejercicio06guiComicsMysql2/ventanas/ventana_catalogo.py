# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_catalogo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_catalogo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_catalogo.setGeometry(QtCore.QRect(20, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_catalogo.setFont(font)
        self.lbl_catalogo.setObjectName("lbl_catalogo")
        self.txt_catalogo = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_catalogo.setGeometry(QtCore.QRect(20, 40, 621, 261))
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
