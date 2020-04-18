from ventanas import ventana_catalogo
from modelo import base



class Ventana_catalogo(ventana_catalogo.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        comics = base.query_select_comics()
        datos = ""
        for c in comics:
            datos += "Id: "+str(c[0])+" / Titulo: "+c[1]+" / Autor: "+c[2]+" / Editorial: "+c[3]+" / Páginas: "+str(c[4])+" / Género: "+c[5]+"\n"
        self.txt_catalogo.setText(datos)
