from ventanas import ventana_principal
from clases_ventanas.clase_ventana_registro import Ventana_registro
from clases_ventanas.clase_ventana_catalogo import Ventana_catalogo
from clases_ventanas.clase_ventana_listado import Ventana_listado
from clases_ventanas.clase_ventana_tabla import Ventana_tabla
from PyQt5 import QtWidgets


class Ventana_principal(ventana_principal.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.subm_registro.triggered.connect(self.abrir_ventana_registro)
        self.subm_catalogo.triggered.connect(self.abrir_ventana_catalogo)
        self.subm_listado.triggered.connect(self.abrir_ventana_listado)
        self.subm_tabla.triggered.connect(self.abrir_ventana_tabla)
        self.subm_salir.triggered.connect(MainWindow.close)
        self.MainWindow = MainWindow

    def abrir_ventana_registro(self):
        self.vr = Ventana_registro()
        self.vr.setupUi(self.MainWindow)
    
    def abrir_ventana_catalogo(self):
        self.vc = Ventana_catalogo()
        self.vc.setupUi(self.MainWindow)
        
    def abrir_ventana_listado(self):
        self.listado = QtWidgets.QMainWindow()
        self.vl = Ventana_listado()
        self.vl.setupUi(self.listado)
         
    def abrir_ventana_tabla(self):
        self.tabla = QtWidgets.QMainWindow()
        self.vt = Ventana_tabla()
        self.vt.setupUi(self.tabla)

        