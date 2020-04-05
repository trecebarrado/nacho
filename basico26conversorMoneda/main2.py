#vamos a usar el archivo generado de la ventana directamente
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_python
import sys
from PyQt5.QtWidgets import QMainWindow


class Conversor_moneda(QMainWindow): 
    def __init__(self):
        super().__init__()     
        self.conversor = ventana_python.Ui_MainWindow()
        self.conversor.setupUi(self)
        self.conversor.boton_convertir_a_dolares.clicked.connect(self.transformar_a_dolares)
        self.conversor.boton_convertir_a_libras.clicked.connect(self.transformar_a_libras)
        self.conversor.boton_convertir_a_yuanes.clicked.connect(self.transformar_a_yuanes)
        self.show()
        
    def transformar_a_dolares(self):
        introducido = self.conversor.entrada_euros.text()
        introducido_float = float(introducido.replace(",","."))
        dolares = round((introducido_float * 1.1), 2)
        self.conversor.label_resultado.setText(str(dolares).replace(".",",")+" Dólares")
        
    def transformar_a_libras(self):
        introducido = self.conversor.entrada_euros.text()
        introducido_float = float(introducido.replace(",","."))
        libras = round((introducido_float * 0.9), 2)
        self.conversor.label_resultado.setText(str(libras).replace(".",",")+" Libras")
         
    def transformar_a_yuanes(self):
        introducido = self.conversor.entrada_euros.text()
        introducido_float = float(introducido.replace(",","."))
        yuanes = round((introducido_float * 7.9), 2)
        self.conversor.label_resultado.setText(str(yuanes).replace(".",",")+" Yuanes")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ventana_python.Ui_MainWindow()
    ui.setupUi(MainWindow)
    convertir = Conversor_moneda()   
    sys.exit(app.exec_())
