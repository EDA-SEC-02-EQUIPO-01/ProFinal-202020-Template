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
                "lista_compañias":None}
    taxitrips["lista_taxis"] = m.newMap(numelements=17, prime=109345121, maptype='CHAINING', loadfactor=0.5, comparefunction=comparar_table)
    taxitrips["lista_compañias"] = m.newMap(numelements=17, prime=109345121, maptype='CHAINING', loadfactor=0.5, comparefunction=comparar_table)
    return taxitrips

# Funciones para agregar informacion al grafo

def addtaxi(catalogo,id):
    pres= m.contains(catalogo["lista_taxis"],id)
    if pres == False:
        m.put(catalogo["lista_taxis"],id,1)
    return catalogo

def addcompany(catalogo,id,company):
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
    addcompany(catalogo,taxiid,company)
    addtaxi(catalogo,taxiid)

# ==============================
# Funciones de consulta
# ==============================

# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================

def comparar_table(route1,route2):
    r2=route2["key"]
    if route1 == r2:
        return 0
    elif route1 > r2:
        return 1
    else:
        return -1
