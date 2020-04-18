from ventanas import ventana_listado
from modelo import base


class Ventana_listado(ventana_listado.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        comics = base.query_select_comics()
        datos = ""
        for c in comics:
            if c[7] == 0:
                colecc = "No"
            else:
                colecc = "Sí"
            datos = "Titulo: "+c[1]+" / Autor: "+c[2]+" / Editorial: "+c[3]+" / Páginas: "+str(c[4])+" / Género: "+c[5]+" / Tapa: "+c[6]+" / coleccion: "+colecc
            self.lst_listado.addItem(datos)
        self.MainWindow = MainWindow
        self.MainWindow.move(400,200)
        self.MainWindow.show()
