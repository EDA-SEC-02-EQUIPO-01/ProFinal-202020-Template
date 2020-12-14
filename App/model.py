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
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.DataStructures import mapentry as ma
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
from DISClib.Algorithms.Sorting import mergesort as mer
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------1

def catalogo():
    taxitrips={"lista_taxis":None,
                "lista_compañias":None,
                "grafo":None}
    taxitrips["lista_taxis"] = m.newMap(numelements=17, prime=109345121, maptype='CHAINING', loadfactor=0.5, comparefunction=comparar_table)
    taxitrips["lista_compañias"] = m.newMap(numelements=17, prime=109345121, maptype='CHAINING', loadfactor=0.5, comparefunction=comparar_table)
    taxitrips["grafo"] = gr.newGraph(datastructure='ADJ_LIST',
                                  directed=False,
                                  size=1000,
                                  comparefunction=comparar_table)

    return taxitrips

# Funciones para agregar informacion al grafo

def addStation(catalogo, area):
    """
    Adiciona una estación como un vertice del grafo
    """
    if not gr.containsVertex(catalogo["grafo"], area):
        gr.insertVertex(catalogo["grafo"], area)
    return catalogo

def addConnection(catalogo,origin, destination,weight):

    gr.addEdge(catalogo["grafo"], origin ,destination , weight)
    return catalogo

def addtaxi(catalogo,id):
    pres= m.contains(catalogo["lista_taxis"],id)
    if pres == False:
        m.put(catalogo["lista_taxis"],id,1)
    return catalogo

def addcompany(catalogo,id,company):
    if company == " ":
        company= "Independent Owner"
    pres= m.contains(catalogo["lista_compañias"],company)
    if pres==False:
        add= {"taxis":1,"servicios":1}
        m.put(catalogo["lista_compañias"],company,add)
    else:
        tpre=m.contains(catalogo["lista_taxis"],id)
        if tpre==False:
            pareja=m.get(catalogo["lista_compañias"],company)
            element=ma.getValue(pareja)
            element["taxis"]+=1
            element["servicios"]+=1
            m.put(catalogo["lista_compañias"],company,element)
        else:
            pareja=m.get(catalogo["lista_compañias"],company)
            element=ma.getValue(pareja)
            element["servicios"]+=1
            m.put(catalogo["lista_compañias"],company,element)
    return catalogo

def addtrip(catalogo,trip):
    taxiid = trip["taxi_id"]
    company = trip['company']
    areainicio= trip["pickup_community_area"]
    areafinal= trip["dropoff_community_area"]
    hour= convert_time(trip["trip_start_timestamp"])
    duration= trip["trip_seconds"]
    addcompany(catalogo,taxiid,company)
    addtaxi(catalogo,taxiid)
    if areainicio != '' and areafinal!= '' and duration != '':
        weight=(hour,convertir_numero(duration))
        addStation(catalogo,areainicio)
        addStation(catalogo,areafinal)
        addConnection(catalogo,areainicio,areafinal,weight)
    
# ==============================
# Funciones de consulta
# ==============================
def mejor_horario(catalogo,areaorigen,areadestino,inicio,fin):
    caminos= djk.Dijkstra(catalogo["grafo"],areaorigen,inicio,fin)
    camino=djk.pathTo(caminos,areadestino)
    return camino

def numero_de_taxis(catalogo):
    total=m.size(catalogo["lista_taxis"])
    return total

def numero_de_compañias(catalogo):
    total=m.size(catalogo["lista_compañias"])
    return total

def top_taxis(catalogo):
    llaves=m.keySet(catalogo["lista_compañias"])
    ite=it.newIterator(llaves)
    lista=lt.newList(datastructure='SINGLE_LINKED', cmpfunction=None)
    while it.hasNext(ite):
        llave=it.next(ite)
        pareja=m.get(catalogo["lista_compañias"],llave)
        lt.addLast(lista,pareja)
    mer.mergesort(lista,comparar_data_taxis)
    return lista

def top_servcios(catalogo):
    llaves=m.keySet(catalogo["lista_compañias"])
    ite=it.newIterator(llaves)
    lista=lt.newList(datastructure='SINGLE_LINKED', cmpfunction=None)
    while it.hasNext(ite):
        llave=it.next(ite)
        pareja=m.get(catalogo["lista_compañias"],llave)
        lt.addLast(lista,pareja)
    mer.mergesort(lista,comparar_data_servicios)
    return lista




# ==============================
# Funciones Helper
# ==============================
def convertir_numero(num):
    numero=""
    for n in range(len(num)):
        if num[n] != ".":
            numero+=num[n]
        else:
            return int(numero)
    return int(numero)



def convert_time(str_boy):
    new_str=str_boy.replace("T"," ")
    conv=datetime.datetime.strptime(new_str,"%Y-%m-%d %H:%M:%S.%f")
    time=conv.time()
    return time
# ==============================
# Funciones de Comparacion
# ==============================

def comparar_data_taxis(com1,com2):
    c1=com1["value"]["taxis"]
    c2=com2["value"]["taxis"]
    if int(c1 < int(c2)):
        return 0
    elif int(c1) > int(c2):
        return 1
    else:
        return -1
def comparar_data_servicios(com1,com2):
    c1=com1["value"]["servicios"]
    c2=com2["value"]["servicios"]
    if int(c1 < int(c2)):
        return 0
    elif int(c1) > int(c2):
        return 1
    else:
        return -1

def comparar_table(route1,route2):
    r2=route2["key"]
    if route1 == r2:
        return 0
    else:
        return -1

def comparar_data(route1,route2):
    r2=route2["key"]
    if (int(route1) == int(r2)):
        return 0
    elif (int(route1) > int(r2)):
        return 1
    else:
        return -1
