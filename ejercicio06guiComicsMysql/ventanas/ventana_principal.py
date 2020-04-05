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
        MainWindow.resize(665, 354)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_titulo.setGeometry(QtCore.QRect(270, 110, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.grv_main = QtWidgets.QGraphicsView(self.centralwidget)
        self.grv_main.setGeometry(QtCore.QRect(0, -20, 231, 381))
        self.grv_main.setStyleSheet("*{background-image: url(\"estilos/batman.png\");}")
        self.grv_main.setObjectName("grv_main")
        self.lbl_subtitulo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_subtitulo.setGeometry(QtCore.QRect(330, 150, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_subtitulo.setFont(font)
        self.lbl_subtitulo.setStyleSheet("* {color: #148CD2;}")
        self.lbl_subtitulo.setObjectName("lbl_subtitulo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu_principal = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.menu_principal.setFont(font)
        self.menu_principal.setObjectName("menu_principal")
        MainWindow.setMenuBar(self.menubar)
        self.subm_registro = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.subm_registro.setFont(font)
        self.subm_registro.setObjectName("subm_registro")
        self.subm_catalogo = QtWidgets.QAction(MainWindow)
        self.subm_catalogo.setObjectName("subm_catalogo")
        self.subm_lista_comics = QtWidgets.QAction(MainWindow)
        self.subm_lista_comics.setObjectName("subm_lista_comics")
        self.subm_tabla_Comics = QtWidgets.QAction(MainWindow)
        self.subm_tabla_Comics.setObjectName("subm_tabla_Comics")
        self.subm_listado = QtWidgets.QAction(MainWindow)
        self.subm_listado.setObjectName("subm_listado")
        self.subm_tabla = QtWidgets.QAction(MainWindow)
        self.subm_tabla.setObjectName("subm_tabla")
        self.subm_salir = QtWidgets.QAction(MainWindow)
        self.subm_salir.setObjectName("subm_salir")
        self.menu_principal.addAction(self.subm_registro)
        self.menu_principal.addAction(self.subm_catalogo)
        self.menu_principal.addAction(self.subm_listado)
        self.menu_principal.addAction(self.subm_tabla)
        self.menu_principal.addSeparator()
        self.menu_principal.addAction(self.subm_salir)
        self.menubar.addAction(self.menu_principal.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " GESTOR COMICS"))
        self.lbl_titulo.setText(_translate("MainWindow", "BIBLIOTECA COMICS"))
        self.lbl_subtitulo.setText(_translate("MainWindow", "Registro y catálogo de Comics."))
        self.menu_principal.setTitle(_translate("MainWindow", "Menú principal"))
        self.subm_registro.setText(_translate("MainWindow", "Registro Comic"))
        self.subm_catalogo.setText(_translate("MainWindow", "Catálogo Comics"))
        self.subm_lista_comics.setText(_translate("MainWindow", "Lista Comics"))
        self.subm_tabla_Comics.setText(_translate("MainWindow", "Tabla Comics"))
        self.subm_listado.setText(_translate("MainWindow", "Listado Comics"))
        self.subm_tabla.setText(_translate("MainWindow", "Tabla Comics"))
        self.subm_salir.setText(_translate("MainWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
