from ventanas import ventana_ficha_comic
from modelo import base
from PyQt5.Qt import QPixmap, QFileDialog, QMessageBox
from functools import partial
from modelo.clases import Comic
import sys
import shutil
from validadores.validacion_datos import validar_texto, validar_paginas, validar_coleccion, validar_tapa
from clases_ventanas import clase_ventana_principal, clase_ventana_tabla


class Ventana_ficha_comic(ventana_ficha_comic.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow):
        global id_fila, id_columna, nombre_columna, valor_celda, comic_selecc, colecc
        super().setupUi(MainWindow)
        fila = clase_ventana_tabla.Ventana_tabla.tbl_tabla.currentRow() #nº fila seleccionada
        id_fila = clase_ventana_tabla.Ventana_tabla.tbl_tabla.item(fila, 0).text() #valor de campo 'Id' según nº de fila seleccionada
        comic_selecc = base.query_select_comic(id_fila)
        self.txt_titulo.setText(comic_selecc.titulo)
        self.txt_autor.setText(comic_selecc.autor)
        self.txt_editorial.setText(comic_selecc.editorial)
        self.txt_genero.setText(comic_selecc.genero)
        self.txt_tapa.setText(comic_selecc.tapa)
        self.txt_paginas.setText(str(comic_selecc.paginas))
        if comic_selecc.coleccion == 0:
            colecc = "No"
        else:
            colecc = "Sí"
        self.txt_coleccion.setText(str(colecc))
        pixmap = QPixmap("portadas/" + str(comic_selecc.id) + ".jpg")
        self.lbl_imagen.setScaledContents(True)
        self.lbl_imagen.setPixmap(pixmap) #muestra imagen seleccionada en el lbl_imagen
        self.btn_editar_portada.setVisible(False) #el botón se activa solo en el modo edición
        self.btn_editar_portada.clicked.connect(partial(self.anadir_portada_comic, id_fila))
        self.btn_editar.clicked.connect(self.editar_comic)
        self.btn_cancelar.setVisible(False) #el botón se activa solo en el modo edición
        self.btn_cancelar.clicked.connect(clase_ventana_tabla.Ventana_tabla.ficha_comic())
        self.btn_guardar.setVisible(False) #el botón se activa solo en el modo edición
        self.btn_guardar.clicked.connect(partial(self.guardar_comic, id_fila))
        self.btn_cerrar.clicked.connect(MainWindow.close)
        self.MainWindow_ficha = MainWindow
        self.MainWindow_ficha.show()
    
    def anadir_portada_comic(self, id_fila): #funcion para añadir portada desde la edición de la ficha
        global ruta_imagen, nueva_imagen
        imagen = QFileDialog.getOpenFileName(self.MainWindow_ficha)
        #guarda en estas variables los datos de la nueva imagen, a expensas que luego se pulse o no en 'Guardar':
        ruta_imagen = imagen[0]
        nueva_imagen = id_fila
        #si se ha elegido una nueva imagen, asigna el Pixmap de la misma al label:
        if ruta_imagen:
            pixmap = QPixmap(ruta_imagen)
            self.lbl_imagen.setPixmap(pixmap)
        
    def editar_comic(self):
        self.btn_editar.setVisible(False) #se desactiva despues de darle y
        self.btn_cancelar.setVisible(True) #se activa sobre él el botón 'Cancelar'
        self.btn_cerrar.setVisible(False) #se desactiva despues de darle y
        self.btn_guardar.setVisible(True) #se activa sobre él el botón 'Guardar'
        # se habilitan los campos como editables, con el texto que haya en amarillo:
        self.txt_titulo.setReadOnly(False)
        self.txt_titulo.setStyleSheet("*{color: yellow;}")
        self.txt_autor.setReadOnly(False)
        self.txt_autor.setStyleSheet("*{color: yellow;}")
        if self.txt_autor.text() == "":
            self.txt_autor.setPlaceholderText("Introduce un dato")
        self.txt_editorial.setReadOnly(False)
        self.txt_editorial.setStyleSheet("*{color: yellow;}")
        if self.txt_editorial.text() == "":
            self.txt_editorial.setPlaceholderText("Introduce un dato")
        self.txt_genero.setReadOnly(False)
        self.txt_genero.setStyleSheet("*{color: yellow;}")
        if self.txt_genero.text() == "":
            self.txt_genero.setPlaceholderText("Introduce un dato")
        self.txt_tapa.setReadOnly(False)
        self.txt_tapa.setStyleSheet("*{color: yellow;}")
        self.txt_paginas.setReadOnly(False)
        self.txt_paginas.setStyleSheet("*{color: yellow;}")
        self.txt_coleccion.setReadOnly(False)
        self.txt_coleccion.setStyleSheet("*{color: yellow;}")
        self.btn_editar_portada.setVisible(True)
        self.btn_editar_portada.setStyleSheet("*{color: yellow;}")
        
    def guardar_comic(self, id_fila):
        comic_datos = Comic()
        comic_datos.id = id_fila
        comic_datos.titulo = self.txt_titulo.text()
        if not validar_texto(comic_datos.titulo):
            QMessageBox.about(self.MainWindow, "Error","El campo Título es incorrecto o no puede estar vacío        ")
            self.txt_titulo.setText(comic_selecc.titulo)
            return
        comic_datos.autor = self.txt_autor.text()
        if comic_datos.autor and not validar_texto(comic_datos.autor):
            QMessageBox.about(self.MainWindow, "Error","El campo Autor es incorrecto        ")
            self.txt_autor.setText(comic_selecc.autor)
            return
        comic_datos.editorial = self.txt_editorial.text()
        if comic_datos.editorial and not validar_texto(comic_datos.editorial):
            QMessageBox.about(self.MainWindow, "Error","El campo Editorial es incorrecto        ")
            self.txt_editorial.setText(comic_selecc.editorial)
            return
        comic_datos.genero = self.txt_genero.text()
        if comic_datos.genero and not validar_texto(comic_datos.genero):
            QMessageBox.about(self.MainWindow, "Error","El campo Editorial es incorrecto        ")
            self.txt_genero.setText(comic_selecc.genero)
            return
        comic_datos.tapa = self.txt_tapa.text().capitalize()
        if not validar_tapa(comic_datos.tapa):
            QMessageBox.about(self.MainWindow, "Error","Indicar 'Blanda' o 'Dura'      ")
            self.txt_tapa.setText(comic_selecc.tapa)
            return
        comic_datos.paginas = str(self.txt_paginas.text())
        if comic_datos.paginas and not validar_paginas(comic_datos.paginas):
            QMessageBox.about(self.MainWindow, "Error","Introduce un nº válido      ")
            self.txt_paginas.setText(str(comic_selecc.paginas))
            return
        dato_coleccion = self.txt_coleccion.text()
        dato_coleccion_format = self.format_valor(dato_coleccion)
        if not validar_coleccion(dato_coleccion_format):
            QMessageBox.about(self.MainWindow, "Error","Indicar 'Sí' o 'No'        ")
            self.txt_coleccion.setText(colecc)
            return
        if dato_coleccion_format == "no":
            comic_datos.coleccion = "0"
        else:
            comic_datos.coleccion = "1"
        base.query_update_ficha(comic_datos)
        try:
            shutil.copy(ruta_imagen,"portadas/" + str(id_fila) + ".jpg")
        except:
            sys.exc_info()
        clase_ventana_principal.Ventana_tabla.ficha_comic()
        self.btn_cerrar.setVisible(True)
        
    def format_valor(self, campo): #formatea el nombre de columna a minúsculas y sin acentos para dárselo a la query
        campo_min = campo.lower()
        reemplazos = (("í","i")) #para eliminar acento de 'paginas'
        for a,b in reemplazos:
            campo_min = campo_min.replace(a,b)
        return campo_min
        