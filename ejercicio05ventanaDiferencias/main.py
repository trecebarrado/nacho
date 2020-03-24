#juego diferencias

import time
#para crear fichero temporal:
import tempfile
from tkinter import *
from tkinter import messagebox as mb

x = 0
y = 0
#contador aciertos:
aciertos = 0
#booleanos para identificar acierto:
dif1 = False 
dif2 = False
dif3 = False
#valor por defecto si no se introduce nombre de jugador:
jugador = "anonimo" 

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
#llama a la funcion que graba la tabla de resultados.
    crea_tabla()
#end juego_resuelto

def crea_tabla():
    grabar = open("tiempos.txt","a")
#el jugador en mayusculas como en las recreativas :)
    grabar.write(jugador.upper()+","+str(tiempo)+"\"\n")
    grabar.close()
#se finaliza juego:
    ventana.destroy()
#end crea_tabla

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
        
def guarda_jugador():
    global jugador
    #recoge dato de jugador la ventana y la borra:
    jugador = entrada.get()
    entrada.delete(0,END)
#end guarda_jugador

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
#si en la lista de resultados hay algo escritto, se ejecuta el siguiente código
#si no, no muestra la tabla de tiempos:
    if lista_ord:
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

def jugar():
    global tini
    tini = time.time()
    registro.destroy()
#end jugar

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

#ventana de registro de jugador:
registro = Toplevel()
registro.geometry("290x70+250+150")
registro.title("REGISTRO JUGADOR")
etiqueta = Label(registro, text="Nombre:")
etiqueta.grid(column=0, row=0, padx=5, pady=5)
entrada = Entry(registro,width=24)
entrada.grid(column=1, row=0, padx=5, pady=5)
boton_registro = Button(registro,text="Registrar", command=guarda_jugador)
boton_registro.grid(column=2, row=0, padx=5, pady=5)
boton_jugar = Button(registro, width=20, text="JUGAR", command=jugar)
boton_jugar.grid(column=1, row=1, padx=5, pady=5)
registro.attributes("-topmost", True)

#llama a la funcion para mostrar mensaje informativo con mejores tiempos:
muestra_tabla()

ventana.bind("<Button 1>", click_raton)
ventana.mainloop()
