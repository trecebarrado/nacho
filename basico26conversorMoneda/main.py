#vamos a usar el archivo generado de la ventana directamente
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_python
import sys

def transformar_a_dolares():
    introducido= ui.entrada_euros.text()
    introducido_float = float(introducido.replace(",","."))
    dolares = round((introducido_float * 1.1), 2)
    ui.label_resultado.setText(str(dolares).replace(".",",")+" Dólares")
    
def transformar_a_libras():
    introducido= ui.entrada_euros.text()
    introducido_float = float(introducido.replace(",","."))
    libras = round((introducido_float * 0.9), 2)
    ui.label_resultado.setText(str(libras).replace(".",",")+" Libras")
    
def transformar_a_yuanes():
    introducido= ui.entrada_euros.text()
    introducido_float = float(introducido.replace(",","."))
    yuanes = round((introducido_float * 7.9), 2)
    ui.label_resultado.setText(str(yuanes).replace(".",",")+" Yuanes")
    
#obligatorio para usar pyqt5:
app = QtWidgets.QApplication(sys.argv)

#se prepara un MainWindow, es parte del protocolo
MainWindow = QtWidgets.QMainWindow()

#crea un objeto de la clase en el archivo generado para preparar la ventana principal (MainWindow)
#para que tenga todo el diseño que tenga en el Designer
ui = ventana_python.Ui_MainWindow()
ui.setupUi(MainWindow)

#todos los widgets y componentes puestos en la ventana por qtdesigner estan en ui
ui.boton_convertir_a_dolares.clicked.connect(transformar_a_dolares)
ui.boton_convertir_a_libras.clicked.connect(transformar_a_libras)
ui.boton_convertir_a_yuanes.clicked.connect(transformar_a_yuanes)

#se muestra la ventana principal de pyqt5
MainWindow.show()
sys.exit(app.exec_())
