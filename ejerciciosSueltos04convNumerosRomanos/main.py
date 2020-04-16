from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal
import sys

dicc = {0:"", 1:"", 2:"X", 3:"C", 4:"M", 50:"L", 500:"D", 100:"C", 1000:"M"}
dicc_r = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def conversor():    
    num = ui.entrada_num.text()
    if num[0] in ("I","V","X","L","C","D","M"):
        ui.label_resultado.setText(conversor_rom(num))
    else:
        ui.label_resultado.setText(conversor_nat(num))
        
def conversor_rom(num):
    long = len(num)
    result = 0
    for i in range(long-1):
        if dicc_r[num[i]] >= dicc_r[num[i+1]]:
            result += dicc_r[num[i]]
        else:
            result -= dicc_r[num[i]]
    obtenido = result + dicc_r[num[long-1]]
    comprobacion = conversor_nat(str(obtenido))
    if num == comprobacion:
        return str(obtenido)
    else:
        return "No es un nº válido"
        
def conversor_nat(num):
    if not(num.isnumeric()) or int(num) == 0 or int(num) > 3999:
        return "No es un nº válido"
    else:
        long = len(num)
        result = ""
        for i in range(long-1):
            if int(num[i]) <= 3:
                result += dicc[long] * int(num[i])
                long -= 1
            elif int(num[i]) == 4:
                result += dicc[long] + dicc[int("5"+"0"*(long-1))]
                long -= 1
            elif int(num[i]) >= 5 and int(num[i]) < 9:
                result += dicc[int("5"+"0"*(long-1))] + (dicc[long] * (int(num[i])-5))
                long -= 1
            elif int(num[i]) == 9:
                result += dicc[long] + dicc[int("1"+"0"*(long))]
                long -= 1
        return result + str(unidades(int(num[-1])))
        
def unidades(num):
    if num <= 3:
        return "I" * num
    elif num == 4:
        return "IV"
    elif num == 9:
        return "IX"
    else:
        return "V" + "I" * (num-5)
    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_principal.Ui_MainWindow()
ui.setupUi(MainWindow)
ui.btn_convertir.clicked.connect(conversor)
MainWindow.show()
sys.exit(app.exec_())