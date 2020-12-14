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

import config as cf
from App import model as m
from DISClib.ADT import map as ma
import csv
from DISClib.ADT.graph import gr
import datetime

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def iniciar_catalogo():
    catalogo=m.catalogo()
    return catalogo

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def loadFile(catalogo, tripfile):

    tripfile = cf.data_dir + tripfile
    input_file = csv.DictReader(open(tripfile, encoding="utf-8"),
                                delimiter=",")
    for trip in input_file:
        m.addtrip(catalogo, trip)
    return catalogo
# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def mejor_horario(catalogo,areaorigen,areadestino,inicio,fin):
    initialDate = datetime.datetime.strptime(inicio, '%H:%M:%S')
    FinalDate = datetime.datetime.strptime(fin, '%H:%M:%S')
    camino=m.mejor_horario(catalogo,areaorigen,areadestino,initialDate.time(),FinalDate.time())
    return camino

def numero_de_taxis(catalogo):
    total= m.numero_de_taxis(catalogo)
    return total
def numero_de_compañias(catalogo):
    total= m.numero_de_compañias(catalogo)
    return total

def top_taxis(catalogo):
    top=m.top_taxis(catalogo)
    return top

def top_servicios(catalogo):
    top=m.top_servcios(catalogo)
    return top
