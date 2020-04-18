from ventanas import ventana_editar_portada
import sys
import shutil
from PyQt5.Qt import QFileDialog
from functools import partial
from clases_ventanas import clase_ventana_tabla


class Ventana_editar_portada(ventana_editar_portada.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow, id_fila):
        super().setupUi(MainWindow)
        self.btn_editar_portada.clicked.connect(partial(self.anadir_portada, id_fila))
        self.MainWindow_editar_portada = MainWindow
        self.MainWindow_editar_portada.show()
        
    def anadir_portada(self, id_fila): #funcion para añadir portada en celdas sin ella
        imagen = QFileDialog.getOpenFileName(self.MainWindow_editar_portada)
        try: #prueba lo siguiente para que no se cierre la aplicación si se cancela la selección de imagen
            ruta = imagen[0]
            shutil.copy(ruta,"portadas/" + str(id_fila) + ".jpg")
            self.MainWindow_editar_portada.close()
            clase_ventana_tabla.Ventana_tabla.ver_portada(id_fila)
            clase_ventana_tabla.Ventana_tabla.recargar_tabla()
        except:
            sys.exc_info()
            