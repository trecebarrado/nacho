from PyQt5 import QtWidgets
from PyQt5.Qt import QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QFile, QTextStream
import sys
from modelo import base
from modelo.clases import Comic
from ventanas import ventana_principal, ventana_registro, ventana_catalogo, ventana_listado, ventana_tabla
import re

def registro_comic():
    comic = Comic()
    titulo = vr.txt_titulo.text()
    autor = vr.txt_autor.text()
    editorial = vr.txt_editorial.text()
    genero = vr.txt_genero.text()
    paginas = vr.txt_paginas.text()
    re_paginas = "\d{1,4}\Z"
    check_paginas = re.match(re_paginas, paginas)
    if not titulo or not autor or not editorial or not genero:
        QMessageBox.about(MainWindow, "Registro","Rellena todos los datos      ")
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
        QMessageBox.about(MainWindow, "Registro","Comic registrado      ")
    else:
        vr.txt_paginas.setText("")
        QMessageBox.about(MainWindow, "Registro","Dato páginas incorrecto      ")

def mostrar_registro():
    vr.setupUi(MainWindow)
    vr.btn_registrar.clicked.connect(registro_comic)
    
def mostrar_catalogo():
    vc.setupUi(MainWindow)
    comics = base.query_select_comics()
    datos = ""
    for c in comics:
        datos += "Id: "+str(c[0])+";   Titulo: "+c[1]+";   Autor: "+c[2]+";   Editorial: "+c[3]+";   Páginas: "+str(c[4])+";   Género: "+c[5]+"\n"
    vc.txt_catalogo.setText(datos)

def mostrar_listado():
    vl.setupUi(MainWindow)
    comics = base.query_select_comics()
    datos = ""
    for c in comics:
        datos = "Id: "+str(c[0])+";   Titulo: "+c[1]+";   Autor: "+c[2]+";   Editorial: "+c[3]+";   Páginas: "+str(c[4])+";   Género: "+c[5]
        vl.lst_listado.addItem(datos)
        
def mostrar_tabla():
    vt.setupUi(MainWindow)
    comics = base.query_select_comics()
    fila = 0
    for c in comics:
        columna = 0
        vt.tbl_tabla.insertRow(fila)
        for e in range(len(c)):
            celda = QTableWidgetItem(str(c[e]))
            vt.tbl_tabla.setItem(fila, columna, celda)
            columna += 1
        fila += 1
    vt.btn_borrar.clicked.connect(borrado_fila)
    vt.btn_cambiar.clicked.connect(cambio_dato)
    
def borrado_fila():
    fila = vt.txt_id.text()
    try:
        int(fila)
        base.query_delete_comic(fila)
        mostrar_tabla()
    except:
        QMessageBox.about(MainWindow, "Info", "Introduce un nº de Id       ")
    
def cambio_dato():
    id_fila = vt.txt_id_fila.text()
    try:
        int(id_fila)
        campo = sin_tilde(vt.txt_campo.text())
        valor = vt.txt_valor.text()
        try:
            base.query_update_comic(campo, valor, id_fila)
            mostrar_tabla()
        except:
            QMessageBox.about(MainWindow, "Info", "Dato de columna no válido       ")
    except:
        QMessageBox.about(MainWindow, "Info", "Introduce un nº de Id       ")

def sin_tilde(campo):
    campo_min = campo.lower()
    reemplazos = (("á","a"), ("é","e"), ("í","i"))
    for a,b in reemplazos:
        campo_min = campo_min.replace(a,b)
    return campo_min
    
def salir_app():
    MainWindow.close()

    
app = QtWidgets.QApplication(sys.argv)

#estilo dark:
file = QFile("estilos\dark.qss")
file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(file)
app.setStyleSheet(stream.readAll())

MainWindow = QtWidgets.QMainWindow()

vp = ventana_principal.Ui_MainWindow()
vr = ventana_registro.Ui_MainWindow()
vc = ventana_catalogo.Ui_MainWindow()
vl = ventana_listado.Ui_MainWindow()
vt = ventana_tabla.Ui_MainWindow()
vp.setupUi(MainWindow)

vp.subm_registro.triggered.connect(mostrar_registro)
vp.subm_catalogo.triggered.connect(mostrar_catalogo)
vp.subm_listado.triggered.connect(mostrar_listado)
vp.subm_tabla.triggered.connect(mostrar_tabla)
vp.subm_salir.triggered.connect(salir_app)

MainWindow.show()
sys.exit(app.exec_())