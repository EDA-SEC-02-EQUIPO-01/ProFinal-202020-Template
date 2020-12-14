"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller as co
from DISClib.ADT import stack
from time import process_time
from DISClib.DataStructures import listiterator as it
import timeit
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""
def convertir_numero(num):
    numero=""
    for n in range(len(num)):
        if num[n] != ".":
            numero+=num[n]
        else:
            return int(numero)
    return int(numero)

def imprimir_top(lista,numero,clave):
    veces=0
    ite=it.newIterator(lista)
    print(f"En el top {numero} de compañias con mayor cantidad de {clave} se encuentran:")
    while it.hasNext(ite) and veces<numero:
        pareja=it.next(ite)
        compañia= pareja["key"]
        taxis=pareja["value"][clave]
        veces+=1
        if veces == (numero):
            print (f"La compañia {compañia} con {taxis} {clave}\n")
        else:
            print (f"La compañia {compañia} con {taxis} {clave}")

def imprimir_pila(pila):
    ite=it.newIterator(pila)
    tiempo=0
    while it.hasNext(ite):
        arco=it.next(ite)
        seg=arco["weight"][1]
        horario=str(arco["weight"][0])
        v1=convertir_numero(arco["vertexA"])
        v2=convertir_numero(arco["vertexB"])
        if tiempo == 0:
            print (f"El mejor horario de inicio de viaje es {horario}\n")
            print (f"La ruta de community areas es la siguiente:")
            print (f"Dea la community area {v1} a la community area {v2}")
            tiempo+=seg
        else:
            print (f"Dea la community area {v1} a la community area {v2}")
            tiempo+=seg
    tiempo= round((tiempo/60),2)
    print(f"El tiempo estimado de viaje es de {tiempo} minutos")


# ___________________________________________________
#  Variables
# ___________________________________________________
small="taxi-trips-wrvz-psew-subset-small.csv"
medium= "taxi-trips-wrvz-psew-subset-medium.csv"
large="taxi-trips-wrvz-psew-subset-large.csv"
# ___________________________________________________
#  Menu principal
# ___________________________________________________

"""
Menu principal
"""
def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Crear analizador")
    print("2- Cargar informacion")
    print("3- Requerimiento 1")
    print("4- Requerimiento 2")
    print("5- Requerimiento 3")
    print("0- Salir")

while True:
    printMenu()
    entrada=input("Seleccione una opcion para continuar\n")

    if int(entrada)==1:
        print("Inicializando...\n")
        time1= process_time()
        cat=co.iniciar_catalogo()
        time2=process_time()
        print(f"Tiempo de ejecucion: {time2-time1} segundos")
    elif int(entrada)==2:
        print("Inicializando...\n")
        time1= process_time()
        co.loadFile(cat,small)
        time2=process_time()
        print(f"Tiempo de ejecucion: {time2-time1} segundos")
    elif int(entrada)==3:
        m=int(input("Ingrese el numero para el top de compañías ordenada por la cantidad de taxis afiliados:\n"))
        n=int(input("Ingrese el numero para el top de de compañías que más servicios prestaron:\n"))
        taxis= co.numero_de_taxis(cat)
        compañias= co.numero_de_compañias(cat)
        top_taxis=co.top_taxis(cat)
        top_servicos=co.top_servicios(cat)
        print(f"En total hay {taxis} taxis\n")
        print(f"En total hay {compañias} compañias\n")
        imprimir_top(top_taxis,m,"taxis")
        imprimir_top(top_taxis,n,"servicios")

    elif int(entrada)==4:
        areainicio=input("Ingrese el area de inicio:\n")
        areafinal=input("Ingrese el area de finalización:\n")
        inicio=input("Ingrese la hora inicial: Formato HH:MM:SS\n")
        fin=input("Ingrese la hora final: Formato HH:MM:SS\n")
        camino=co.mejor_horario(cat,areainicio+".0",areafinal+".0",inicio, fin)
        imprimir_pila(camino)
    elif int(entrada)==0:
        break
