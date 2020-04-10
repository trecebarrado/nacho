# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_nueva_tabla.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
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
        self.lbl_tabla = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tabla.setGeometry(QtCore.QRect(22, 3, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tabla.setFont(font)
        self.lbl_tabla.setObjectName("lbl_tabla")
        self.tbl_tabla = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_tabla.setGeometry(QtCore.QRect(22, 34, 621, 281))
        self.tbl_tabla.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tbl_tabla.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tbl_tabla.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_tabla.setAlternatingRowColors(False)
        self.tbl_tabla.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_tabla.setObjectName("tbl_tabla")
        self.tbl_tabla.setColumnCount(6)
        self.tbl_tabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tabla.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tabla.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tabla.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tabla.setHorizontalHeaderItem(5, item)
        self.tbl_tabla.horizontalHeader().setDefaultSectionSize(100)
        self.tbl_tabla.horizontalHeader().setMinimumSectionSize(30)
        self.tbl_tabla.horizontalHeader().setStretchLastSection(True)
        self.tbl_tabla.verticalHeader().setDefaultSectionSize(22)
        self.tbl_tabla.verticalHeader().setMinimumSectionSize(21)
        self.tbl_tabla.setColumnHidden(0, True)
        header = self.tbl_tabla.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.btn_borrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_borrar.setGeometry(QtCore.QRect(473, 320, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_borrar.setFont(font)
        self.btn_borrar.setObjectName("btn_borrar")
        self.btn_cambiar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cambiar.setGeometry(QtCore.QRect(292, 320, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_cambiar.setFont(font)
        self.btn_cambiar.setObjectName("btn_cambiar")
        self.btn_click = QtWidgets.QPushButton(self.centralwidget)
        self.btn_click.setGeometry(QtCore.QRect(-2, -2, 670, 360))
        self.btn_click.setStyleSheet("* {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.btn_click.setText("")
        self.btn_click.setObjectName("btn_click")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(23, 35, 32, 29))
        self.btn_clear.setStyleSheet("* {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    min-width: 1px;\n"
"}")
        self.btn_clear.setText("")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_click.raise_()
        self.lbl_tabla.raise_()
        self.tbl_tabla.raise_()
        self.btn_borrar.raise_()
        self.btn_cambiar.raise_()
        self.btn_clear.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_cambiar, self.btn_borrar)
        MainWindow.setTabOrder(self.btn_borrar, self.tbl_tabla)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " GESTOR COMICS - Tabla"))
        self.lbl_tabla.setText(_translate("MainWindow", "Tabla datos Comics:"))
        self.tbl_tabla.setSortingEnabled(True)
        item = self.tbl_tabla.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tbl_tabla.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Título"))
        item = self.tbl_tabla.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Autor"))
        item = self.tbl_tabla.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Editorial"))
        item = self.tbl_tabla.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Páginas"))
        item = self.tbl_tabla.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Género"))
        self.btn_borrar.setText(_translate("MainWindow", "Borrar fila actual"))
        self.btn_cambiar.setText(_translate("MainWindow", "Editar dato seleccionado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
