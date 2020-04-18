from ventanas import ventana_tabla
from PyQt5.Qt import Qt, QMessageBox, QTableWidgetItem, QPushButton, QMenu, QApplication
from modelo import base
from pathlib import Path
import os
from PyQt5 import QtGui, QtWidgets, QtCore
from functools import partial
from clases_ventanas.clase_ventana_ficha_comic import Ventana_ficha_comic
from clases_ventanas.clase_ventana_editar_dato import Ventana_editar_dato
from clases_ventanas.clase_ventana_ver_portada import Ventana_ver_portada
from clases_ventanas.clase_ventana_editar_portada import Ventana_editar_portada

class Ventana_tabla(ventana_tabla.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.cargar_tabla()
        self.btn_reord.clicked.connect(self.recargar_tabla) #limpia la ventana al recargarla
        self.btn_reord.setToolTip("Ordenar por Id") #info emergente botón
        self.btn_deselecc.clicked.connect(self.borrar_seleccion_tabla) #llama a la funcion para borrar elemento seleccionado
        self.tbl_tabla.itemClicked.connect(self.habilitar_botones_tabla) #al pinchar en la tabla, llama a la funcion que habilita los botones de la ventana
        self.tbl_tabla.setContextMenuPolicy(Qt.CustomContextMenu) #menú contextual de la tabla
        self.tbl_tabla.customContextMenuRequested.connect(self.menu_contextual_tabla) #llama a funcion del menú contextual
        self.tbl_tabla.itemDoubleClicked.connect(self.ficha_comic) #abre la ventana ficha cómic
        self.btn_ver.setEnabled(False) #hasta que se seleccione un elemento de la tabla, el botón está inhabilitado
        self.btn_ver.clicked.connect(self.ficha_comic)
        self.btn_editar.setEnabled(False) #hasta que se seleccione un elemento de la tabla, el botón está inhabilitado
        self.btn_editar.clicked.connect(self.edicion_dato) #abre la ventana que edita el dato seleccionado
        self.btn_borrar.setEnabled(False) #hasta que se seleccione un elemento de la tabla, el botón está inhabilitado
        self.btn_borrar.clicked.connect(self.borrado_fila) 
        self.MainWindow_tabla = MainWindow
        self.MainWindow_tabla.move(420,220)
        self.MainWindow_tabla.show()
        
    def borrar_seleccion_tabla(self): #limpia la selecion e inhabilita botones:
        self.tbl_tabla.clearSelection()
        self.btn_ver.setEnabled(False)
        self.btn_editar.setEnabled(False)
        self.btn_borrar.setEnabled(False)
         
    def habilitar_botones_tabla(self): #funcion llamada si se pincha en la tabla
        self.btn_ver.setEnabled(True)
        self.btn_editar.setEnabled(True)
        self.btn_borrar.setEnabled(True)
     
    def menu_contextual_tabla(self, position):
        self.habilitar_botones_tabla()
        id_columna = self.tbl_tabla.currentColumn() #recoge nº de la columna seleccionada
        fila = self.tbl_tabla.currentRow() #recoge nº de fila seleccionada
        id_fila = self.tbl_tabla.item(fila, 0).text() #valor de la columna 'Id' de la fila seleccionada
        if id_columna < 7: #en todas las columnas salvo la 7 el menu tiene opciones 'Editar' y 'Copiar':
            menu = QMenu()
            opcion_copiar = menu.addAction("Copiar")
            opcion_editar = menu.addAction("Editar")
            opcion_ver = menu.addAction("Ver cómic")
            seleccion = menu.exec_(self.tbl_tabla.mapToGlobal(position))
            if seleccion == opcion_copiar:       
                QApplication.clipboard().setText(self.tbl_tabla.currentItem().text()) #copia dato al portapapeles
            elif seleccion == opcion_editar:       
                self.edicion_dato() #llama funcion de editar
            elif seleccion == opcion_ver:
                self.ficha_comic()
        elif id_columna == 7 and not Path("portadas/" + str(id_fila) + ".jpg").is_file(): #en columna 7 (Portadas) solo se muestra opción 'Editar':
            menu = QMenu()
            opcion = menu.addAction("Editar")
            seleccion = menu.exec_(self.tbl_tabla.mapToGlobal(position))
            if seleccion == opcion:
                self.edicion_dato()
        
    def cargar_tabla(self): #crea tabla con la query correspondiente:
        comics = base.query_select_comics()
        fila = 0
        for c in comics:
            self.tbl_tabla.insertRow(fila)
            columna = 0
            for e in range(7):
                celda = QTableWidgetItem(str(c[e]))
                self.tbl_tabla.setItem(fila, columna, celda)
                columna += 1
            img = "portadas/" + str(c[0]) + ".jpg"
            if Path(img).is_file(): #si en la fila correspondiente hay imagen guardada, crea el botón para mostrarla:
                btn_miniatura = QPushButton(" Ampliar")
                ico = QtGui.QIcon() #se crea icono de la portada que llevará el botón
                ico.addPixmap(QtGui.QPixmap(img), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                btn_miniatura.setIcon(ico)
                btn_miniatura.setStyleSheet("*{min-width: 1px;") #evita restricción del ancho de los botones a 80px de la hoja de estilo dark
                btn_miniatura.clicked.connect(partial(self.ver_portada, c[0])) #llama a la funcion para ampliar portada en nueva ventana, pasando su Id
                self.tbl_tabla.setCellWidget(fila, columna, btn_miniatura)
            else: #si el Id no tiene imagen:
                valor = QTableWidgetItem("Sin portada")
                self.tbl_tabla.setItem(fila, columna, valor)
            fila += 1
    
    def recargar_tabla(self):
        self.setupUi(self.MainWindow_tabla)
        
    def edicion_dato(self): #edición celda de la tabla
        global id_fila, id_columna, nombre_columna, valor_celda
        fila = self.tbl_tabla.currentRow() #nº fila seleccionada
        id_fila = self.tbl_tabla.item(fila, 0).text() #valor de campo 'Id' según nº de fila seleccionada
        id_columna = self.tbl_tabla.currentColumn() #nº columna seleccionada
        nombre_columna = self.tbl_tabla.horizontalHeaderItem(id_columna).text() #nombre del encabezado de la columna segun nº columna seleccionada
        valor_celda = self.tbl_tabla.currentItem().text() #valor celda seleccionada
        if id_columna == 7: #si es la columna 7 (Portadas), abre la ventana editar_portada
            self.editar_portada()
        else: #para el resto de columnas, abre la ventana editar_dato
            self.editar_dato()
             
    def borrado_fila(self): #borrado fila de la tabla
        global fila, id_fila
        fila = self.tbl_tabla.currentRow()
        id_fila = self.tbl_tabla.item(fila, 0).text()
        #se crea MessageBox personalizado de confirmación de borrado:
        confirmacion = QMessageBox(self)
        confirmacion.setIcon(QMessageBox.Warning)
        confirmacion.setWindowTitle("Confirmación")
        confirmacion.setInformativeText("¿Seguro que deseas borrar\nla fila " + str(fila+1) + "?")
        confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        confirmacion.setDefaultButton(QMessageBox.Cancel)
        boton_yes = confirmacion.button(QMessageBox.Yes)
        boton_yes.setText("Aceptar")
        boton_cancel = confirmacion.button(QMessageBox.Cancel)
        boton_cancel.setText("Cancelar")
        respuesta = confirmacion.exec_()
        if respuesta == QMessageBox.Yes:
            base.query_delete_comic(id_fila)
            if Path("portadas/" + str(id_fila) + ".jpg").is_file():
                os.remove("portadas/" + str(id_fila) + ".jpg")
            self.setupUi(self.MainWindow_tabla)
             
    def editar_dato(self):
        self.editar_dato = QtWidgets.QMainWindow(None, QtCore.Qt.WindowStaysOnTopHint) #ventana edición celdas de la tabla
        self.ved = Ventana_editar_dato()
        self.ved.setupUi(self.editar_dato, id_fila, id_columna, nombre_columna, valor_celda)
     
    def editar_portada(self):
        self.editar_portada = QtWidgets.QMainWindow() #ventana edición portadas
        self.vep = Ventana_editar_portada()
        self.vep.setupUi(self.editar_portada, id_fila)
     
    def ver_portada(self, id_imagen):
        self.portada = QtWidgets.QMainWindow() #ventana ficha cómic
        self.vvp = Ventana_ver_portada()
        self.vvp.setupUi(self.portada, id_imagen)
         
    def ficha_comic(self):
        self.comic = QtWidgets.QMainWindow() #ventana ficha cómic
        self.vfc = Ventana_ficha_comic()
        self.vfc.setupUi(self.comic)
