from ventanas import ventana_editar_dato
from validadores.validacion_datos import validar_paginas, validar_tapa, validar_texto
from PyQt5.Qt import QMessageBox
from modelo import base
from clases_ventanas import clase_ventana_tabla
from functools import partial


class Ventana_editar_dato(ventana_editar_dato.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow, id_columna, id_fila, nombre_columna, valor_celda):
        super().setupUi(MainWindow)
        if nombre_columna == "Pág.":
            self.lbl_editar_dato.setText("Editar 'Páginas':")
        else:
            self.lbl_editar_dato.setText("Editar '" + nombre_columna + "':")
        self.txt_editar_dato.setText(valor_celda)
        self.btn_editar_dato.clicked.connect(partial(self.guardar_dato, id_columna, id_fila, nombre_columna, valor_celda)) #llama a la funcion que valida y registra el cambio
        self.MainWindow_editar_dato = MainWindow
        self.MainWindow_editar_dato.show()
        
    def guardar_dato(self, id_fila, id_columna, nombre_columna, valor_celda): #funcion que valida y registra la edicion de datos de la tabla
        columna = self.format_valor(nombre_columna) #llama a la funcion que formatea el nombre de la columna
        valor = self.txt_editar_dato.text()
        if id_columna == 4: #validador columna Páginas
            columna = "paginas" #asigna el nombre de la columna ya que en la tabla es 'Pág.'
            if valor and not validar_paginas(valor): #se puede dejar vacío (queda a 0)
                QMessageBox.about(self.MainWindow_editar_dato, "Error","Introduce un nº válido      ")
                self.txt_editar_dato.setText(valor_celda)
                return
        elif id_columna == 6:
                valor = valor.capitalize()
                if not validar_tapa(valor): #validador columna Tapa
                    QMessageBox.about(self.MainWindow_editar_dato, "Error","Indicar 'Blanda' o 'Dura'      ")
                    return
        elif id_columna == 1 and not validar_texto(valor): #validador columna Título
                QMessageBox.about(self.MainWindow_editar_dato, "Error","El dato es incorrecto o no puede estar vacío        ")
                self.txt_editar_dato.setText(valor_celda)
                return
        elif valor and not validar_texto(valor): #validador resto columnas. Se pueden dejar vacías
            QMessageBox.about(self.MainWindow_editar_dato, "Error","El dato es incorrecto        ")
            self.txt_editar_dato.setText(valor_celda)
            return
        base.query_update_comic(columna, valor, id_fila)
        self.MainWindow_editar_dato.close()
         
    def format_valor(self, campo): #formatea el nombre de columna a minúsculas y sin acentos para dárselo a la query
        campo_min = campo.lower()
        reemplazos = (("é","e"), ("í","i")) #para eliminar acentos de 'género' y 'título'
        for a,b in reemplazos:
            campo_min = campo_min.replace(a,b)
        return campo_min
