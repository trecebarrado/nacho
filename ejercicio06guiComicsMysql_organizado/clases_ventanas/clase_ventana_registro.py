from ventanas import ventana_registro
from PyQt5.Qt import QFileDialog, QPixmap, QMessageBox
import shutil
import sys
from modelo.clases import Comic
from validadores.validacion_datos import validar_texto
from modelo import base


class Ventana_registro(ventana_registro.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.btn_imagen.clicked.connect(self.seleccionar_imagen)
        self.btn_registrar.clicked.connect(self.registro_comic)
        self.MainWindow = MainWindow

    def seleccionar_imagen(self): #selección de imagen de ventana de registro
        imagen = QFileDialog.getOpenFileName(self.MainWindow) #explorador para seleccionar imagen, guarda en var imagen su ruta
        ruta_imagen = imagen[0] #la ruta está en el primer elemento de una lista de tuplas
        try: #prueba lo siguiente para que no se cierre la aplicación si se cancela el explorador de selección de imagen
            shutil.copy(ruta_imagen,"temp/img_temp.jpg") #se copia la imagen al directorio temp
            self.lbl_imagen.setStyleSheet("*{background-image: url(""); border:1px solid #32414B;}") 
            pixmap = QPixmap("temp/img_temp.jpg")
            self.lbl_imagen.setScaledContents(True)
            self.lbl_imagen.setPixmap(pixmap) #muestra imagen seleccionada en el lbl_imagen
        except:
            sys.exc_info()
            
    def registro_comic(self): #función de registro nuevo cómic
        comic = Comic() #se crea objeto de la clase Comic
        #asignación de valores y validaciones:
        comic.titulo = self.txt_titulo.text()
        if not validar_texto(comic.titulo):
            QMessageBox.about(self.MainWindow, "Error","El campo Título es incorrecto o no puede estar vacío        ")
            self.txt_titulo.setText("")
            return
        comic.autor = self.txt_autor.text()
        if comic.autor and not validar_texto(comic.autor): #"if comic.autor" para que se pueda dejar el campo en blanco (no es obligatorio)
            QMessageBox.about(self.MainWindow, "Error","El campo Autor es incorrecto        ")
            self.txt_autor.setText("")
            return
        comic.editorial = self.txt_editorial.text()
        if comic.editorial and not validar_texto(comic.editorial):
            QMessageBox.about(self.MainWindow, "Error","El campo Editorial es incorrecto        ")
            self.txt_editorial.setText("")
            return
        comic.paginas = self.spb_paginas.value() #SpinBox de nº de páginas
        genero_selecc = self.cmb_genero.currentIndex() #ComboBox de Género
        comic.genero = self.cmb_genero.itemText(genero_selecc)
        if self.rdb_blanda.isChecked(): #RadioButtons de Tapa
            comic.tapa = "Blanda"
        if self.rdb_cartone.isChecked():
            comic.tapa = "Dura"
        if self.chb_coleccion.isChecked():
            comic.coleccion = True
        id_generado = base.query_insert_comic(comic) #variable id_generado guarda el valor de 'Id' para nombrar la imagen
        try:
            ruta_portada = "portadas/" + str(id_generado) + ".jpg"
            shutil.move("temp/img_temp.jpg", ruta_portada)
        except:
            sys.exc_info()
        QMessageBox.about(self.MainWindow, "Info","Cómic registrado        ")
        self.setupUi(self.MainWindow) #limpia la ventana al recaragarla

    
