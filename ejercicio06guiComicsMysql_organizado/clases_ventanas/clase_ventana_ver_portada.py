from ventanas import ventana_ver_portada
from PyQt5.Qt import QPixmap, QFileDialog
import shutil
from functools import partial
import sys
import os
from PyQt5 import QtCore
from clases_ventanas import clase_ventana_tabla


class Ventana_ver_portada(ventana_ver_portada.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow, id_imagen):
        super().setupUi(MainWindow)
        pixmap = QPixmap("portadas/" + str(id_imagen) + ".jpg")
        self.lbl_img_portada.setPixmap(pixmap)
        self.btn_cambiar_portada.clicked.connect(partial(self.cambiar_portada, id_imagen)) #botón 'Cambiar' portada
        self.btn_borrar_portada.clicked.connect(partial(self.borrar_portada, id_imagen)) #botón 'Borrar' portada
        self.btn_cerrar_portada.clicked.connect(MainWindow.close) #botón 'Cerrar' portada
        self.MainWindow_ver_portada = MainWindow
        self.MainWindow_ver_portada.show()

    def cambiar_portada(self, id_imagen): #cambio de imagen de la portada
        imagen = QFileDialog.getOpenFileName(self.MainWindow_ver_portada)
        try: #prueba lo siguiente para que no se cierre la aplicación si se cancela la selección de imagen
            ruta = imagen[0]
            shutil.copy(ruta,"portadas/" + str(id_imagen) + ".jpg")
            pixmap = QPixmap("portadas/" + str(id_imagen) + ".jpg")
            self.lbl_img_portada.setPixmap(pixmap)
            clase_ventana_tabla.Ventana_tabla.recargar_tabla()
        except:
            sys.exc_info()
             
    def borrar_portada(self, id_imagen): #borra imagen de la portada
        try:
            os.remove("portadas/" + str(id_imagen) + ".jpg")
            self.lbl_img_portada.clear()
            self.lbl_img_portada.setStyleSheet("*{font-family: verdana; font-size: 14px;}")
            self.lbl_img_portada.setAlignment(QtCore.Qt.AlignCenter)
            self.lbl_img_portada.setText("Sin Portada")
            clase_ventana_tabla.Ventana_tabla.recargar_tabla()
        except:
            sys.exc_info()
            
    
