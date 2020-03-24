#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

def introduccion():
    print("\n##### EL REINO DEL DRAGÓN ######")
    print("\nEstamos en el Reino del Dragón. En él hay una cueva con")
    print("dos Dragones dormidos que custodian grandes tesoros. Según el")
    print("humor con que se despierten, compartirán el tesoro contigo...")
    print("o te comerán en cuanto te vean!\n")
    print("VIDAS: "+str(vidas)+"\n")
    
def puentes():
    print("Fase 2:")
    print("Te topas con un enorme cortado del que no se ve el fondo.")
    print("para sortearlo, hay dos maltrechos puentes de cuerda y maderos.")

def cavernas():
    print("Fase 3:")
    print("Llegas frente a dos cavernas. Al fondo de cada una de ellas hay un")
    print("enorme Dragón dormido, y tras ellos, sendos tesoros...")
    
def salidas():
    print("Fase final:")
    print("Debes huir con tu tesoro antes de que el Dragón cambie de humor...")
    print("Ves un río que desemboca en el exterior y te zambulles en él.")
    print("El río se divide, llevando el agua por dos diferentes salidas.")
    
def elegirEntrada():
    entrada = ""
    while entrada != "1" and entrada != "2":
        print("Fase 1:")
        print("Estás frente a la cueva, en su interior dos caminos se bifurcan.")
        print("¿Qué camino eliges, 1 o 2?")
        entrada = input()
    return entrada
    
def elegirPuente():
    puente = ""
    while puente != "1" and puente != "2":
        print("¿Qué puente eliges, 1 o 2?")
        puente = input()
    return puente
    
def elegirCaverna():
    caverna = ""
    while caverna != "1" and caverna != "2":
        print("¿A qué caverna entras, 1 o 2?")
        caverna = input()
    return caverna

def elegirSalida():
    salida = ""
    while salida != "1" and salida != "2":
        print("¿Qué salida eliges, 1 o 2?")
        salida = input()
    return salida
    
def cheqEntrada(elegirEntrada):
    global superadaEntrada, vidas, puntuacion, continuar
    print("\nTe adentras por el camino...")
    time.sleep(2)
    print("Está oscuro y tenebroso...")
    time.sleep(2)
    print("Arena y rocas empiezan a caer a tu paso...\n")
    time.sleep(2)
    correctaEntrada = random.randint (1, 2)
    if elegirEntrada == str(correctaEntrada):
        puntuacion += 100
        superadaEntrada = True
        print("esquivas las rocas y consigues avanzar!\n")
        print("Encuentras 100 monedas de oro.\n")
        time.sleep(2)
    else:
        vidas -= 1
        continuar = False
        print("y la cueva se desmorona sobre ti...\n")
        print("GAME OVER\n")

def cheqPuente(elegirPuente):
    global superadaPuente, vidas, puntuacion, continuar
    print("\nComienzas a cruzar el puente...")
    time.sleep(2)
    print("Se mueve y chirría...")
    time.sleep(2)
    print("Oyes como se resquebraja...\n")
    time.sleep(2)
    buenPuente = random.randint (1, 2)
    if elegirPuente == str(buenPuente):
        puntuacion += 100
        superadaPuente = True
        print("pero consigues llegar al otro lado!\n")
        print("Encuentras 100 monedas de oro.\n")
        time.sleep(2)
    else:
        vidas -= 1
        continuar = False
        print("pisas en un tablón roto y caes al vacío.\n")
        print("GAME OVER\n")

def cheqCaverna(elegirCaverna):
    global superadaCaverna, vidas, puntuacion, continuar
    print("\nEntras en la caverna...")
    time.sleep(2)
    print("Huesos de otros aventureros crujen bajo tus pies...")
    time.sleep(2)
    print("El gran Dragón abre sus ojos, salta delante tuyo y...\n")
    time.sleep(2)
    correctaCaverna = random.randint (1, 2)
    if elegirCaverna == str(correctaCaverna):
        puntuacion += 300
        superadaCaverna = True
        print("te entrega 300 monedas de oro!\n")
        time.sleep(2)
    else:
        vidas -= 1
        continuar = False
        print("te come de un bocado!\n")
        print("GAME OVER\n")
        
def cheqSalida(elegirSalida):
    global superadaSalida, vidas, puntuacion, continuar
    print("\nLa corriente te arrastra...")
    time.sleep(2)
    print("Nadas con fuerza hacia una de las salidas...")
    time.sleep(2)
    print("Caes por una cascada al exterior de la cueva y...\n")
    time.sleep(2)
    correctaSalida = random.randint (1, 2)
    if elegirSalida == str(correctaSalida):
        puntuacion += 100
        superadaSalida = True
        print("¡¡Enhorabuena!!")
        print("consigues llegar ileso hasta la orilla del río.\n")
        print("Encuentras 100 monedas de oro.\n")
        time.sleep(2)
    else:
        vidas -= 1
        continuar = False
        print("te golpeas contra unas rocas y te ahogas.\n")
        print("GAME OVER\n")

empezarNuevo = ("si")
puntuacion = 0
vidas = 5
superadaEntrada = False
superadaPuente = False
superadaCaverna = False
superadaSalida = False

introduccion()

while empezarNuevo == ("s") or empezarNuevo == ("si"):
    
    seguir = ("si")
    continuar = True
    
    while continuar == True and vidas in range(1,6) and superadaSalida == False:
        
        if superadaEntrada == False:
            numEntrada = elegirEntrada()
            cheqEntrada(numEntrada)
            if continuar == False:
                break
            
        if superadaPuente == False:      
            puentes()
            numPuente = elegirPuente()
            cheqPuente(numPuente)
            if continuar == False:
                break
            
        if superadaCaverna == False:
            cavernas()
            numCaverna = elegirCaverna()
            cheqCaverna(numCaverna)
            if continuar == False:
                break
            
        if superadaSalida == False:
            salidas()
            numSalida = elegirSalida()
            cheqSalida(numSalida)
            if continuar == False:
                break
            
        print("Tu tesoro es de "+str(puntuacion)+" monedas de oro.\n")
        print("¿Quieres volver a la cueva para acumular más riquezas? (si o no)")
        seguir = input()
        print("")
        if seguir == ("s") or seguir == ("si"):
            superadaEntrada = False
            superadaPuente = False
            superadaCaverna = False
            superadaSalida = False
            empezarNuevo = ("si")

    if vidas == 0:
        print("No te quedan vidas.")
        break

    elif superadaSalida == True:
        break
    
    else:
        print("Vidas restantes: "+str(vidas))
        print("¿Continuar partida? (si o no)")
        empezarNuevo = input()
        print("")
        if empezarNuevo == ("s") or empezarNuevo == ("si"):
            puntuacion -= 100
            if puntuacion >= 0:
                print("Pierdes 100 monedas")
                print("Total monedas: "+str(puntuacion)+"\n")     
            else:
                puntuacion = 0
                print("Total monedas: 0\n")
                time.sleep(1)

if puntuacion < 0:
    puntuacion = 0      
print("Total monedas: "+str(puntuacion))       
print("\n¡Adiós!")

