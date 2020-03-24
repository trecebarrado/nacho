#juego diferencias

import time
#para crear fichero temporal:
import tempfile
from tkinter import *
from tkinter import messagebox as mb

x = 0
y = 0
jugador = ""
#contador aciertos:
aciertos = 0
#booleanos para identificar acierto:
dif1 = False 
dif2 = False
dif3 = False

def click_raton(evento):
    global aciertos, dif1, dif2, dif3
    x = evento.x
    y = evento.y
    if x >= 456 and x <= 502 and y >= 157 and y <= 196 and aciertos < 3:
        if dif1 == True:
#funcion diferencia ya encontrada:
            ya_encontrada()
        else:
            aciertos += 1
            dif1 = True
            if aciertos == 3:
#funcion para todas las diferencias encontradas:
                juego_resuelto()
            else:
#funcion para acierto diferencia:
                evento_acierto()
    elif x >= 532 and x <= 569 and y >= 6 and y <= 46 and aciertos < 3:
        if dif2 == True:
            ya_encontrada()
        else:
            aciertos += 1
            dif2 = True
            if aciertos == 3:
                juego_resuelto()
            else:
                evento_acierto()
    elif x >= 388 and x <= 453 and y >= 175 and y <= 187 and aciertos < 3:
        if dif3 == True:
            ya_encontrada()
        else:
            aciertos += 1
            dif3 = True
            if aciertos == 3:
                juego_resuelto()
            else:
                evento_acierto()
#si no se da ningun caso:
    else:
        mb.showwarning(title="Juego diferencias", message="""
        NO HAY DIFERENCIA
        
        """+ str(3 - aciertos) +""" POR ENCONTRAR""")      
#end click_raton

def juego_resuelto():
    global tiempo
    #cálculo tiempo tardado:
    tfin = time.time()
    tiempo_total = float(tfin - tini)
#formateo del tiempo para guardarlo con 6 posiciones: 3 digitos (completados con
#ceros a la izqda para poder ser ordenados como str) mas el punto y 2 decimales:
    tiempo = "{:0>6.2f}".format(tiempo_total)
    mb.showinfo(title="Juego diferencias", message="""
    ¡ENHORABUENA, ENCONTRASTE LAS 3 DIFERENCIAS!
    
    TIEMPO TOTAL: """+str(round(tiempo_total,2))+"""\"
    
    FIN DEL JUEGO""")
#llama a la funcion para mostrar la ventana de registro:   
    ventana_registro()
#end juego_resuelto

#ventana de registro de jugador:
def ventana_registro():
    global registro, entrada
    registro = Toplevel()
    registro.geometry()
    registro.title("Juego diferencias")
    etiqueta_info = Label(registro, text="Graba tu tiempo:")
    etiqueta_info.grid(column=0, row=0, columnspan=2, padx=3, pady=3, sticky=W)
    etiqueta_nombre = Label(registro, text="Nombre:")
    etiqueta_nombre.grid(column=0, row=1, padx=3, pady=3, sticky=W)
    entrada = Entry(registro,width=24)
    entrada.grid(column=1, row=1, padx=3, pady=3)
    boton_registro = Button(registro,text="Grabar", command=graba_jugador)
    boton_registro.grid(column=2, row=1, padx=3, pady=3)
    boton_cancelar = Button(registro,text="Cancelar", command=salir_sin_grabar)
    boton_cancelar.grid(column=1, row=2, padx=3, pady=3, sticky=W+E)
    registro.attributes("-topmost", True)
#end ventana_registro

def graba_jugador():
    global jugador
    jugador = entrada.get()
#llama a la funcion que graba la tabla de resultados.
    crea_tabla()
    registro.destroy()
#llama a la funcion para mostrar mejores tiempos ordenados:
    muestra_tabla()
#se finaliza juego:
    ventana.destroy()
#end graba_jugador

def salir_sin_grabar():
    registro.destroy()
    muestra_tabla()
    ventana.destroy()
#end salir_sin_grabar

def crea_tabla():
    global jugador
    if not jugador:
        jugador = "anonimo"
    grabar = open("tiempos.txt","a")
#el jugador en mayusculas como en las recreativas :)
    grabar.write(jugador.upper()+","+str(tiempo)+"\"\n")
    grabar.close()
#end crea_tabla

def muestra_tabla():
#lee los datos de los resultados y los guarda en una lista por pares:
    lectura = open("tiempos.txt","r")
    lista_ord = []
    for l in lectura:
        lista = l.split(",")
        lista_ord.append(lista)
#se ordena la lista por el 2ª elemento de cada par:
    lista_ord.sort(key = lambda i : i[1])
    lectura.close()
#se crea un fichero temporal para guardar los datos formateados:
    lista_form = tempfile.TemporaryFile(mode = "w+t")
    posicion = 0
    for i in lista_ord:
        for n in range(0,2,2):
#graba los 10 mejores resultados:
            if posicion == 10:
                break
            posicion += 1
            nombre = i[n]
            record = i[n+1]
#escribe los datos formateados (posicion, nombre y tiempo):
            lista_form.write("{:2d}".format(posicion)+". "+nombre+" - Tiempo: "+record.lstrip("0"))
#pinta el nº de posiciones vacías hasta la 10:
    resto_pos = 10 - posicion
    for n in range(resto_pos):
        posicion += 1
        lista_form.write("{:2d}".format(posicion)+".\n")
#se pone al principio del fichero y lee y muestra los datos en un messagebox:
    lista_form.seek(0)
    texto = lista_form.read()
    tabla = Toplevel()
    tabla.withdraw()
    mb.showinfo(title="TABLA TIEMPOS", message=texto)
#destruye el fichero temporal:
    lista_form.close()
#end muestra_tabla

def evento_acierto():
#tiempo parcial al acertar una diferencia:
    tinter = time.time()
    tiempo_parcial = float(tinter - tini)
#se informa del nº de aciertos por encontrar
    mb.showinfo(title="Juego diferencias", message="""
    ¡DIFERENCIA ENCONTRADA!
    
    """+ str(3 - aciertos) +""" POR ENCONTRAR
    
    TIEMPO: """+str(round(tiempo_parcial,2))+"""\"""")
#end evento_acierto

def ya_encontrada():
    mb.showwarning(title="Juego diferencias", message="""
    DIFERENCIA YA ENCONTRADA
    
    """+ str(3 - aciertos) +""" POR ENCONTRAR""") #se informa del nº de aciertos por encontrar
#end ya_encontrada

#ventana principal:
ventana = Tk()
ventana.geometry("696x263")
ventana.title("ENCUENTRA LAS 3 DIFERENCIAS")
canvas = Canvas(ventana, width=692, height=259)
canvas.pack(expand=YES, fill=BOTH)
imagen = PhotoImage(file="imagen.png")
canvas.create_image(0, 0, image=imagen, anchor=NW)

mb.showinfo(title="Juego diferencias", message="""
ENCUENTRA LAS 3 DIFERENCIAS EN LA IMAGEN DE LA DERECHA""")

#se inicia el tiempo al cerrar la ventana informativa:
tini = time.time()

ventana.bind("<Button 1>", click_raton)
ventana.mainloop()
