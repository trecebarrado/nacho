from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QMenu, QApplication
from PyQt5.QtCore import QFile, QTextStream, Qt
import sys
from modelo import base
from modelo.clases import Comic
from ventanas import ventana_principal, ventana_registro, ventana_catalogo, ventana_nueva_tabla, ventana_nueva_listado, ventana_cambio
import re


def mostrar_registro():
    vr.setupUi(MainWindow)
    vr.btn_registrar.clicked.connect(registro_comic)
    
def registro_comic():
    comic = Comic()
    titulo = vr.txt_titulo.text()
    autor = vr.txt_autor.text()
    editorial = vr.txt_editorial.text()
    genero = vr.txt_genero.text()
    paginas = vr.txt_paginas.text()
    re_paginas = "\d{1,4}\Z"
    check_paginas = re.match(re_paginas, paginas)
    if not titulo:
        QMessageBox.about(MainWindow, "Registro", "El campo Título no puede estar vacío        ")
    elif check_paginas:
        comic.titulo = titulo
        comic.autor = autor
        comic.editorial = editorial
        comic.genero = genero
        comic.paginas = paginas
        base.query_insert_comic(comic)
        vr.txt_titulo.setText("")
        vr.txt_autor.setText("")
        vr.txt_editorial.setText("")
        vr.txt_paginas.setText("")
        vr.txt_genero.setText("")
        QMessageBox.about(MainWindow, "Registro","Comic registrado        ")
    else:
        QMessageBox.about(MainWindow, "Registro","Dato páginas incorrecto        ")

def mostrar_catalogo():
    vc.setupUi(MainWindow)
    comics = base.query_select_comics()
    datos = ""
    for c in comics:
        datos += "Id: "+str(c[0])+",   Titulo: "+c[1]+",   Autor: "+c[2]+",   Editorial: "+c[3]+",   Páginas: "+str(c[4])+",   Género: "+c[5]+",\n"
    vc.txt_catalogo.setText(datos)

def mostrar_inicio():
    vp.setupUi(MainWindow)
    vp.subm_registro.triggered.connect(mostrar_registro)
    vp.subm_catalogo.triggered.connect(mostrar_catalogo)
    vp.subm_listado.triggered.connect(abrir_listado)
    vp.subm_tabla.triggered.connect(cargar_tabla)
    vp.subm_inicio.triggered.connect(mostrar_inicio)
    vp.subm_salir.triggered.connect(salir_app)
    
def salir_app():
    MainWindow.close()

def abrir_listado():
    vnl.setupUi(listado)
    comics = base.query_select_comics()
    datos = ""
    for c in comics:
        datos = "Titulo: "+c[1]+"   Autor: "+c[2]+"   Editorial: "+c[3]+"   Páginas: "+str(c[4])+"   Género: "+c[5]
        vnl.lst_listado.addItem(datos)
    listado.show()
    
def cargar_tabla():
    vnt.setupUi(tabla)
    crear_tabla()
    vnt.tbl_tabla.itemClicked.connect(hablitar)
    vnt.tbl_tabla.itemDoubleClicked.connect(cambiar_dato)
    vnt.tbl_tabla.setContextMenuPolicy(Qt.CustomContextMenu)
    vnt.tbl_tabla.customContextMenuRequested.connect(menu)
    tabla.show()

def menu(position):
    menu = QMenu()
    boton_derecho1 = menu.addAction("Editar")
    boton_derecho2 = menu.addAction("Copiar")
    seleccion = menu.exec_(vnt.tbl_tabla.mapToGlobal(position))
    if seleccion == boton_derecho1:
        cambiar_dato()
    elif seleccion == boton_derecho2:       
        QApplication.clipboard().setText(vnt.tbl_tabla.currentItem().text())
        
def hablitar():
    vnt.btn_cambiar.setEnabled(True)
    vnt.btn_borrar.setEnabled(True)

def crear_tabla():
    comics = base.query_select_comics()
    fila = 0
    for c in comics:
        columna = 0
        vnt.tbl_tabla.insertRow(fila)
        for e in range(len(c)):
            celda = QTableWidgetItem(str(c[e]))
            vnt.tbl_tabla.setItem(fila, columna, celda)
            columna += 1
        fila += 1
    vnt.btn_cambiar.setEnabled(False)
    vnt.btn_cambiar.clicked.connect(cambiar_dato)
    vnt.btn_borrar.setEnabled(False)
    vnt.btn_borrar.clicked.connect(borrar_fila)
    vnt.btn_click.clicked.connect(click)
    vnt.btn_clear.clicked.connect(clear)

def click():
    vnt.tbl_tabla.clearSelection()
    vnt.btn_cambiar.setEnabled(False)
    vnt.btn_borrar.setEnabled(False)
    
def clear():
    cargar_tabla()

def borrar_fila():
    global fila, id_fila
    fila = vnt.tbl_tabla.currentRow()
    id_fila = vnt.tbl_tabla.item(fila, 0).text()
    confirmar_borrado()
        
def cambiar_dato():
    global id_fila, id_columna, nombre_columna, valor_celda
    fila = vnt.tbl_tabla.currentRow()
    id_columna = vnt.tbl_tabla.currentColumn()
    id_fila = vnt.tbl_tabla.item(fila, 0).text()
    nombre_columna = vnt.tbl_tabla.horizontalHeaderItem(id_columna).text()
    valor_celda = vnt.tbl_tabla.currentItem().text()
    abrir_cambio()
    
def abrir_cambio():
    vnc.setupUi(cambio)
    vnc.txt_cambio.setText(valor_celda)
    vnc.btn_cambio.clicked.connect(comprobar_cambio)
    cambio.show()

def comprobar_cambio():
    global valor
    valor = vnc.txt_cambio.text()
    valor_bool = bool(valor)
    if id_columna == 4:
        try:
            int(valor_celda)
            int(valor)
            guardar_cambio()
        except:
            QMessageBox.about(cambio, "Error","Dato páginas incorrecto        ")
    elif valor_bool == False and id_columna == 1:
        QMessageBox.about(cambio, "Error","El campo Título no puede estar vacío        ")
    else:
        guardar_cambio()

def guardar_cambio():
    columna = sin_tilde(nombre_columna)
    base.query_update_comic(columna, valor, id_fila)
    cargar_tabla()
    cambio.close()

def sin_tilde(campo):
    campo_min = campo.lower()
    reemplazos = (("á","a"), ("é","e"), ("í","i"))
    for a,b in reemplazos:
        campo_min = campo_min.replace(a,b)
    return campo_min
    
def confirmar_borrado():
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
        cargar_tabla()


app = QtWidgets.QApplication(sys.argv)

#estilo dark:
hoja_estilo = QFile("estilos\dark.qss")
hoja_estilo.open(QFile.ReadOnly | QFile.Text)
leer = QTextStream(hoja_estilo)
app.setStyleSheet(leer.readAll())

MainWindow = QtWidgets.QMainWindow()
vp = ventana_principal.Ui_MainWindow()

mostrar_inicio()

vr = ventana_registro.Ui_MainWindow()
vc = ventana_catalogo.Ui_MainWindow()

listado = QtWidgets.QMainWindow()
vnl = ventana_nueva_listado.Ui_MainWindow()
listado.move(400,200)

tabla = QtWidgets.QMainWindow()
vnt = ventana_nueva_tabla.Ui_MainWindow()
tabla.move(420,220)

cambio = QtWidgets.QMainWindow(None, QtCore.Qt.WindowStaysOnTopHint)
vnc = ventana_cambio.Ui_MainWindow()

MainWindow.show()
sys.exit(app.exec_())