from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QMenu, QApplication, QFileDialog, QPixmap, QPushButton
from PyQt5.QtCore import QFile, QTextStream, Qt
import sys
from modelo import base
from modelo.clases import Comic
from ventanas import ventana_principal, ventana_registro, ventana_catalogo, ventana_tabla, ventana_listado, \
ventana_editar_dato, ventana_editar_portada, ventana_ver_comic,\
    ventana_ver_portada
from validadores.validacion_datos import validar_texto, validar_paginas, validar_tapa,\
    validar_coleccion
from _functools import partial
import shutil
from pathlib import Path
import os

img_selecc = False #a True si al registrar se selecciona una imagen. Permite registrar sin imagen
img_anadida = False #a True si al editar se selecciona una imagen. Permite editar sin imagen

def abrir_ventana_inicio(): #abre ventana principal de la aplicación
    vvpp.setupUi(MainWindow)
    #menú principal:
    vvpp.subm_registro.triggered.connect(abrir_ventana_registro)
    vvpp.subm_catalogo.triggered.connect(abrir_ventana_catalogo)
    vvpp.subm_listado.triggered.connect(abrir_ventana_listado)
    vvpp.subm_tabla.triggered.connect(abrir_ventana_tabla)
    vvpp.subm_salir.triggered.connect(MainWindow.close)

def abrir_ventana_registro(): #abre ventana de registro de nuevo cómic
    vr.setupUi(MainWindow)
    vr.btn_imagen.clicked.connect(seleccionar_imagen)
    vr.btn_registrar.clicked.connect(registro_comic)
    
def seleccionar_imagen(): #selección de imagen de ventana de registro
    global img_selecc
    imagen = QFileDialog.getOpenFileName(MainWindow) #explorador para seleccionar imagen, guarda en var imagen su ruta
    ruta_imagen = imagen[0] #la ruta está en el primer elemento de una lista de tuplas
    try: #prueba lo siguiente para que no se cierre la aplicación si se cancela el explorador de selección de imagen
        shutil.copy(ruta_imagen,"temp/img_temp.jpg") #se copia la imagen al directorio temp
        vr.lbl_imagen.setStyleSheet("*{background-image: url(""); border:1px solid #32414B;}") 
        pixmap = QPixmap("temp/img_temp.jpg")
        vr.lbl_imagen.setScaledContents(True)
        vr.lbl_imagen.setPixmap(pixmap) #muestra imagen seleccionada en el lbl_imagen
        img_selecc = True #se cambia el valor a True pues se ha seleccionado una imagen
    except:
        sys.exc_info()
    
def registro_comic(): #función de registro nuevo cómic
    global img_selecc
    comic = Comic() #se crea objeto de la clase Comic
    #asignación de valores y validaciones:
    comic.titulo = vr.txt_titulo.text()
    if not validar_texto(comic.titulo):
        QMessageBox.about(MainWindow, "Error","El campo Título es incorrecto o no puede estar vacío        ")
        vr.txt_titulo.setText("")
        return
    comic.autor = vr.txt_autor.text()
    if comic.autor and not validar_texto(comic.autor): #"if comic.autor" para que se pueda dejar el campo en blanco (no es obligatorio)
        QMessageBox.about(MainWindow, "Error","El campo Autor es incorrecto        ")
        vr.txt_autor.setText("")
        return
    comic.editorial = vr.txt_editorial.text()
    if comic.editorial and not validar_texto(comic.editorial):
        QMessageBox.about(MainWindow, "Error","El campo Editorial es incorrecto        ")
        vr.txt_editorial.setText("")
        return
    comic.paginas = vr.spb_paginas.value() #SpinBox de nº de páginas
    genero_selecc = vr.cmb_genero.currentIndex() #ComboBox de Género
    comic.genero = vr.cmb_genero.itemText(genero_selecc)
    if vr.rdb_blanda.isChecked(): #RadioButtons de Tapa
        comic.tapa = "Blanda"
    if vr.rdb_cartone.isChecked():
        comic.tapa = "Dura"
    if vr.chb_coleccion.isChecked():
        comic.coleccion = True
    id_generado = base.query_insert_comic(comic) #variable id_generado guarda el valor de 'Id' para nombrar la imagen
    if img_selecc: #solo se ejecuta lo siguiente si se ha seleccionado imagen y por tanto la variable es True
        ruta_portada = "portadas/" + str(id_generado) + ".jpg"
        shutil.move("temp/img_temp.jpg", ruta_portada)
    QMessageBox.about(MainWindow, "Info","Cómic registrado        ")
    abrir_ventana_registro() #limpia la ventana al recargarla
    img_selecc = False #se vuelve a poner a False de cara al proximo registro

def abrir_ventana_catalogo(): #ventana con datos de la base en un TextEdit
    vc.setupUi(MainWindow)
    comics = base.query_select_comics()
    datos = ""
    for c in comics:
        datos += "Id: "+str(c[0])+" / Titulo: "+c[1]+" / Autor: "+c[2]+" / Editorial: "+c[3]+" / Páginas: "+str(c[4])+" / Género: "+c[5]+"\n"
    vc.txt_catalogo.setText(datos)

def abrir_ventana_listado(): #ventana independiente con datos de la base en un ListWidget
    vl.setupUi(listado)
    comics = base.query_select_comics()
    datos = ""
    for c in comics:
        if c[7] == 0:
            colecc = "No"
        else:
            colecc = "Sí"
        datos = "Titulo: "+c[1]+" / Autor: "+c[2]+" / Editorial: "+c[3]+" / Páginas: "+str(c[4])+" / Género: "+c[5]+" / Tapa: "+c[6]+" / coleccion: "+colecc
        vl.lst_listado.addItem(datos)
    listado.show()
    
def abrir_ventana_tabla(): #ventana independiente con datos de la base en un TableWidget
    vt.setupUi(tabla)
    cargar_tabla()
    vt.btn_reord.clicked.connect(abrir_ventana_tabla) #limpia la ventana al recargarla
    vt.btn_reord.setToolTip("Ordenar por Id") #info emergente botón
    vt.btn_deselecc.clicked.connect(borrar_seleccion_tabla) #llama a la funcion para borrar elemento seleccionado
    vt.tbl_tabla.itemClicked.connect(habilitar_botones_tabla) #al pinchar en la tabla, llama a la funcion que habilita los botones de la ventana
    vt.tbl_tabla.setContextMenuPolicy(Qt.CustomContextMenu) #menú contextual de la tabla
    vt.tbl_tabla.customContextMenuRequested.connect(menu_contextual_tabla) #llama a funcion del menú contextual
    vt.tbl_tabla.itemDoubleClicked.connect(edicion_dato)
    vt.btn_ver.setEnabled(False) #hasta que se seleccione un elemento de la tabla, el botón está inhabilitado
    vt.btn_ver.clicked.connect(ver_comic)
    vt.btn_editar.setEnabled(False) #hasta que se seleccione un elemento de la tabla, el botón está inhabilitado
    vt.btn_editar.clicked.connect(edicion_dato)
    vt.btn_borrar.setEnabled(False) #hasta que se seleccione un elemento de la tabla, el botón está inhabilitado
    vt.btn_borrar.clicked.connect(borrado_fila)
    tabla.show()
    
def borrar_seleccion_tabla(): #limpia la selecion e inhabilita botones:
    vt.tbl_tabla.clearSelection()
    vt.btn_ver.setEnabled(False)
    vt.btn_editar.setEnabled(False)
    vt.btn_borrar.setEnabled(False)
    
def habilitar_botones_tabla(): #funcion llamada si se pincha en la tabla
    vt.btn_ver.setEnabled(True)
    vt.btn_editar.setEnabled(True)
    vt.btn_borrar.setEnabled(True)

def menu_contextual_tabla(position):
    habilitar_botones_tabla()
    id_columna = vt.tbl_tabla.currentColumn() #recoge nº de la columna seleccionada
    fila = vt.tbl_tabla.currentRow() #recoge nº de fila seleccionada
    id_fila = vt.tbl_tabla.item(fila, 0).text() #valor de la columna 'Id' de la fila seleccionada
    if id_columna < 7: #en todas las columnas salvo la 7 el menu tiene opciones 'Editar' y 'Copiar':
        menu = QMenu()
        boton_derecho1 = menu.addAction("Copiar")
        boton_derecho2 = menu.addAction("Editar")
        boton_derecho3 = menu.addAction("Ver cómic")
        seleccion = menu.exec_(vt.tbl_tabla.mapToGlobal(position))
        if seleccion == boton_derecho1:       
            QApplication.clipboard().setText(vt.tbl_tabla.currentItem().text()) #copia dato al portapapeles
        elif seleccion == boton_derecho2:       
            edicion_dato() #llama funcion de editar
        elif seleccion == boton_derecho3:
            ver_comic()
    elif id_columna == 7 and not Path("portadas/" + str(id_fila) + ".jpg").is_file(): #en columna 7 (Portadas) solo se muestra opción 'Editar':
        menu = QMenu()
        boton_derecho = menu.addAction("Editar")
        seleccion = menu.exec_(vt.tbl_tabla.mapToGlobal(position))
        if seleccion == boton_derecho:
            edicion_dato()
    
def cargar_tabla(): #crea tabla con la query correspondiente:
    comics = base.query_select_comics()
    fila = 0
    for c in comics:
        vt.tbl_tabla.insertRow(fila)
        columna = 0
        for e in range(7):
            celda = QTableWidgetItem(str(c[e]))
            vt.tbl_tabla.setItem(fila, columna, celda)
            columna += 1
        img = "portadas/" + str(c[0]) + ".jpg"
        if Path(img).is_file(): #si en la fila correspondiente hay imagen guardada, crea el botón para mostrarla:
            btn_miniatura = QPushButton(" Ampliar")
            ico = QtGui.QIcon() #se crea icono de la portada que llevará el botón
            ico.addPixmap(QtGui.QPixmap(img), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            btn_miniatura.setIcon(ico)
            btn_miniatura.setStyleSheet("*{min-width: 1px;") #evita restricción del ancho de los botones a 80px de la hoja de estilo dark
            btn_miniatura.clicked.connect(partial(ver_portada, c[0])) #llama a la funcion para ampliar portada en nueva ventana, pasando su Id
            vt.tbl_tabla.setCellWidget(fila, columna, btn_miniatura)
        else: #si el Id no tiene imagen:
            valor = QTableWidgetItem("Sin portada")
            vt.tbl_tabla.setItem(fila, columna, valor)
        fila += 1
        
def ver_comic(): #abre la ventana para listar cómic
    global id_fila, id_columna, nombre_columna, valor_celda
    vvc.setupUi(comic)
    fila = vt.tbl_tabla.currentRow() #nº fila seleccionada
    id_fila = vt.tbl_tabla.item(fila, 0).text() #valor de campo 'Id' según nº de fila seleccionada
    comic_selecc = base.query_select_comic(id_fila)
    vvc.txt_titulo.setText(comic_selecc.titulo)
    vvc.txt_autor.setText(comic_selecc.autor)
    vvc.txt_editorial.setText(comic_selecc.editorial)
    vvc.txt_genero.setText(comic_selecc.genero)
    vvc.txt_tapa.setText(comic_selecc.tapa)
    vvc.txt_paginas.setText(str(comic_selecc.paginas))
    if comic_selecc.coleccion == 0:
        colecc = "No"
    else:
        colecc = "Sí"
    vvc.txt_coleccion.setText(str(colecc))
    pixmap = QPixmap("portadas/" + str(comic_selecc.id) + ".jpg")
    vvc.lbl_imagen.setScaledContents(True)
    vvc.lbl_imagen.setPixmap(pixmap) #muestra imagen seleccionada en el lbl_imagen
    vvc.btn_editar_portada.setVisible(False) #el botón se activa solo en el modo edición
    vvc.btn_editar_portada.clicked.connect(partial(anadir_portada_comic, id_fila))
    vvc.btn_editar.clicked.connect(editar_comic)
    vvc.btn_cancelar.setVisible(False) #el botón se activa solo en el modo edición
    vvc.btn_cancelar.clicked.connect(ver_comic)
    vvc.btn_guardar.setVisible(False) #el botón se activa solo en el modo edición
    vvc.btn_guardar.clicked.connect(partial(guardar_comic, id_fila))
    vvc.btn_cerrar.clicked.connect(comic.close)
    comic.show()

def editar_comic():
    vvc.btn_editar.setVisible(False) #se desactiva despues de darle y
    vvc.btn_cancelar.setVisible(True) #se activa sobre él el botón 'Cancelar'
    vvc.btn_cerrar.setVisible(False) #se desactiva despues de darle y
    vvc.btn_guardar.setVisible(True) #se activa sobre él el botón 'Guardar'
    vvc.btn_editar_portada.setVisible(True)
    # se habilitan los campos como editables, con el texto en amarillo:
    vvc.btn_editar_portada.setStyleSheet("*{color: yellow;}")
    vvc.txt_titulo.setReadOnly(False)
    vvc.txt_titulo.setStyleSheet("*{color: yellow;}")
    vvc.txt_autor.setReadOnly(False)
    vvc.txt_autor.setStyleSheet("*{color: yellow;}")
    vvc.txt_editorial.setReadOnly(False)
    vvc.txt_editorial.setStyleSheet("*{color: yellow;}")
    vvc.txt_genero.setReadOnly(False)
    vvc.txt_genero.setStyleSheet("*{color: yellow;}")
    vvc.txt_tapa.setReadOnly(False)
    vvc.txt_tapa.setStyleSheet("*{color: yellow;}")
    vvc.txt_paginas.setReadOnly(False)
    vvc.txt_paginas.setStyleSheet("*{color: yellow;}")
    vvc.txt_coleccion.setReadOnly(False)
    vvc.txt_coleccion.setStyleSheet("*{color: yellow;}")
    
def guardar_comic(id_fila):
    global img_anadida
    try: #permite cancelar la edidión
        comic_datos = Comic()
        comic_datos.id = id_fila
        comic_datos.titulo = vvc.txt_titulo.text()
        if not validar_texto(comic_datos.titulo):
            QMessageBox.about(comic, "Error","El campo Título es incorrecto o no puede estar vacío        ")
            vvc.txt_titulo.setText(comic_datos.titulo)
            return
        comic_datos.autor = vvc.txt_autor.text()
        if comic_datos.autor and not validar_texto(comic_datos.autor):
            QMessageBox.about(comic, "Error","El campo Autor es incorrecto        ")
            vvc.txt_editorial.setText(comic_datos.autor)
            return
        comic_datos.editorial = vvc.txt_editorial.text()
        if comic_datos.editorial and not validar_texto(comic_datos.editorial):
            QMessageBox.about(comic, "Error","El campo Editorial es incorrecto        ")
            vvc.txt_editorial.setText(comic_datos.editorial)
            return
        comic_datos.genero = vvc.txt_genero.text()
        if comic_datos.genero and not validar_texto(comic_datos.genero):
            QMessageBox.about(comic, "Error","El campo Editorial es incorrecto        ")
            vvc.txt_editorial.setText(comic_datos.genero)
            return
        comic_datos.tapa = vvc.txt_tapa.text()
        if not validar_tapa(comic_datos.tapa):
            QMessageBox.about(comic, "Error","Indicar 'Blanda' o 'Dura'      ")
            vvc.txt_editorial.setText(comic_datos.tapa)
            return
        comic_datos.paginas = str(vvc.txt_paginas.text())
        if comic_datos.paginas and not validar_paginas(comic_datos.paginas): #se puede dejar vacío (queda a 0)
            QMessageBox.about(comic, "Error","Introduce un nº válido      ")
            vvc.txt_paginas.setText(comic_datos.paginas)
        dato_coleccion = vvc.txt_coleccion.text()
        if not validar_coleccion(dato_coleccion):
            QMessageBox.about(comic, "Error","Indicar 'Sí' o 'No'        ")
            return
        if dato_coleccion == "No":
            comic_datos.coleccion = "0"
        elif dato_coleccion == "Sí":
            comic_datos.coleccion = "1"
        base.query_update_comic_ver(comic_datos)
        if img_anadida == True:
            shutil.copy(ruta_imagen,"portadas/" + str(id_fila) + ".jpg")
            img_anadida = False
        ver_comic()
        abrir_ventana_tabla()
        vvc.btn_cerrar.setVisible(True)
    except:
        ver_comic()
        abrir_ventana_tabla()
        vvc.btn_cerrar.setVisible(True)
        
def anadir_portada_comic(id_fila): #funcion para añadir portada en celdas sin ella
    global img_anadida
    img_anadida = False
    global ruta_imagen, nueva_imagen
    imagen = QFileDialog.getOpenFileName(editar_portada)
    ruta_imagen = imagen[0]
    try: #prueba lo siguiente para que no se cierre la aplicación si se cancela la selección de imagen
        nueva_imagen = id_fila
        pixmap = QPixmap(ruta_imagen)
        vvc.lbl_imagen.setPixmap(pixmap)
        img_anadida = True
    except:
        pixmap = QPixmap("portadas/" + str(id_fila) + ".jpg")
        vvc.lbl_imagen.setScaledContents(True)
        vvc.lbl_imagen.setPixmap(pixmap)
        
def edicion_dato(): #edición celda de la tabla
    global id_fila, id_columna, nombre_columna, valor_celda
    fila = vt.tbl_tabla.currentRow() #nº fila seleccionada
    id_fila = vt.tbl_tabla.item(fila, 0).text() #valor de campo 'Id' según nº de fila seleccionada
    id_columna = vt.tbl_tabla.currentColumn() #nº columna seleccionada
    nombre_columna = vt.tbl_tabla.horizontalHeaderItem(id_columna).text() #nombre del encabezado de la columna segun nº columna seleccionada
    valor_celda = vt.tbl_tabla.currentItem().text() #valor celda seleccionada
    if id_columna == 7: #si es la columna 7 (Portadas), abre la ventana editar_portada
        vep.setupUi(editar_portada)
        vep.btn_editar_portada.clicked.connect(anadir_portada)
        editar_portada.show()
    else: #para el resto de columnas, abre la ventana editar_dato
        ved.setupUi(editar_dato)
        ved.lbl_editar_dato.setText("Editar '" + nombre_columna + "':")
        ved.txt_editar_dato.setText(valor_celda)
        ved.btn_editar_dato.clicked.connect(guardar_dato) #llama a la funcion que valida y registra el cambio
        editar_dato.show()
        
def anadir_portada(): #funcion para añadir portada en celdas sin ella
    imagen = QFileDialog.getOpenFileName(editar_portada)
    ruta = imagen[0]
    try: #prueba lo siguiente para que no se cierre la aplicación si se cancela la selección de imagen
        shutil.copy(ruta,"portadas/" + str(id_fila) + ".jpg")
        editar_portada.close()
        ver_portada(id_fila)
        abrir_ventana_tabla() #recarga ventana para ver los cambios
    except:
        sys.exc_info()
        
def guardar_dato(): #funcion que valida y registra la edicion de datos de la tabla
    columna = format_columna(nombre_columna) #llama a la funcion que formatea el nombre de la columna
    valor = ved.txt_editar_dato.text()
    if id_columna == 4: #validador columna Páginas
        columna = "paginas" #asigna el nombre de la columna ya que en la tabla es 'Pág.'
        if valor and not validar_paginas(valor): #se puede dejar vacío (queda a 0)
            QMessageBox.about(editar_dato, "Error","Introduce un nº válido      ")
            ved.txt_editar_dato.setText(valor_celda)
            return
    elif id_columna == 6 and not validar_tapa(valor): #validador columna Tapas
            QMessageBox.about(editar_dato, "Error","Indicar 'Blanda' o 'Dura'      ")
            return
    elif id_columna == 1 and not validar_texto(valor): #validador columna Título
            QMessageBox.about(editar_dato, "Error","El dato es incorrecto o no puede estar vacío        ")
            ved.txt_editar_dato.setText(valor_celda)
            return
    elif valor and not validar_texto(valor): #validador resto columnas. Se pueden dejar vacías
        QMessageBox.about(editar_dato, "Error","El dato es incorrecto        ")
        ved.txt_editar_dato.setText(valor_celda)
        return
    base.query_update_comic(columna, valor, id_fila)
    abrir_ventana_tabla() #recarga la tabla para actualizar cambios
    editar_dato.close()

def format_columna(campo): #formatea el nombre de columna a minúsculas y sin acentos para dárselo a la query
    campo_min = campo.lower()
    reemplazos = (("é","e"), ("í","i")) #para eliminar acentos de columnas 'género' y 'título'
    for a,b in reemplazos:
        campo_min = campo_min.replace(a,b)
    return campo_min
        
def borrado_fila(): #borrado fila de la tabla
    global fila, id_fila
    fila = vt.tbl_tabla.currentRow()
    id_fila = vt.tbl_tabla.item(fila, 0).text()
    #se crea MessageBox personalizado de confirmación de borrado:
    confirmacion = QMessageBox(tabla)
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
        abrir_ventana_tabla()
        
def ver_portada(id_imagen): #abre la ventana que muestra la portada ampliada
    vvp.setupUi(portada)
    pixmap = QPixmap("portadas/" + str(id_imagen) + ".jpg")
    vvp.lbl_img_portada.setPixmap(pixmap)
    vvp.btn_cambiar_portada.clicked.connect(partial(cambiar_portada, id_imagen)) #botón 'Cambiar' portada
    vvp.btn_borrar_portada.clicked.connect(partial(borrar_portada, id_imagen)) #botón 'Borrar' portada
    vvp.btn_cerrar_portada.clicked.connect(portada.close) #botón 'Cerrar' portada
    portada.show()
    
def cambiar_portada(id_imagen): #cambio de imagen de la portada
    imagen = QFileDialog.getOpenFileName(editar_portada)
    ruta = imagen[0]
    try: #prueba lo siguiente para que no se cierre la aplicación si se cancela la selección de imagen
        shutil.copy(ruta,"portadas/" + str(id_imagen) + ".jpg")
        pixmap = QPixmap("portadas/" + str(id_imagen) + ".jpg")
        vvp.lbl_img_portada.setPixmap(pixmap)
        abrir_ventana_tabla()
    except:
        sys.exc_info()
        
def borrar_portada(id_imagen): #borra imagen de la portada
    os.remove("portadas/" + str(id_imagen) + ".jpg")
    vvp.lbl_img_portada.clear()
    vvp.lbl_img_portada.setStyleSheet("*{font-family: verdana; font-size: 14px;}")
    vvp.lbl_img_portada.setAlignment(QtCore.Qt.AlignCenter)
    vvp.lbl_img_portada.setText("Sin Portada")
    abrir_ventana_tabla()
        

app = QtWidgets.QApplication(sys.argv)

#hoja estilo qss:
hoja_estilo = QFile("estilos\dark.qss")
hoja_estilo.open(QFile.ReadOnly | QFile.Text)
leer = QTextStream(hoja_estilo)
app.setStyleSheet(leer.readAll())

MainWindow = QtWidgets.QMainWindow() #ventana principal de la aplicación
vvpp = ventana_principal.Ui_MainWindow()
abrir_ventana_inicio()

vr = ventana_registro.Ui_MainWindow() #ventana de registro de nuevo cómic

vc = ventana_catalogo.Ui_MainWindow() #ventana con datos de la base en un TextEdit

listado = QtWidgets.QMainWindow() #ventana independiente con datos de la base en un ListWidget
vl = ventana_listado.Ui_MainWindow()
listado.move(400,200)

tabla = QtWidgets.QMainWindow() #ventana independiente con datos de la base en un TableWidget
vt = ventana_tabla.Ui_MainWindow()
tabla.move(420,220)

editar_dato = QtWidgets.QMainWindow(None, QtCore.Qt.WindowStaysOnTopHint) #ventana edición celdas de la tabla
ved = ventana_editar_dato.Ui_MainWindow()

portada = QtWidgets.QMainWindow() #ventana que muestra la portada seleccionada en grande
vvp = ventana_ver_portada.Ui_MainWindow()

editar_portada = QtWidgets.QMainWindow() #ventana edición portadas
vep = ventana_editar_portada.Ui_MainWindow()

comic = QtWidgets.QMainWindow() #ventana ver cómic
vvc = ventana_ver_comic.Ui_MainWindow()

MainWindow.show()
sys.exit(app.exec_())