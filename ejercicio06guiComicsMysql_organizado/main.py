from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, QTextStream
import sys
from clases_ventanas import clase_ventana_principal


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    hoja_estilo = QFile("estilos\dark.qss") #hoja estilo qss
    hoja_estilo.open(QFile.ReadOnly | QFile.Text)
    fichero = QTextStream(hoja_estilo)
    app.setStyleSheet(fichero.readAll())
    MainWindow = QtWidgets.QMainWindow()
    vpp = clase_ventana_principal.Ventana_principal()
    vpp.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

