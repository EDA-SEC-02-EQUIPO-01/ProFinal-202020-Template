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
import timeit
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________
small="taxi-trips-wrvz-psew-subset-small.csv"
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
    elif int(entrada)==4:
        None
    elif int(entrada)==5:
        None
    elif int(entrada)==0:
        break
