import os
import json
import time 
import pyodbc
import queries
import compiler
import configuracion

#Valor de Conexión Default:

#Conexión a Base
#PRUEBAS
#cadena_conexion = compiler.do(configuracion.connF)

#!!!!!Producción
cadena_conexion = compiler.do(configuracion.connP)



conexion_input = input("Conexión (local/produccion): ")
print("La conexión es: ", conexion_input)

if(conexion_input == "pruebas"):
    cadena_conexion = compiler.do(configuracion.connF)
elif(conexion_input == "produccion"):
    cadena_conexion = compiler.do(configuracion.connP)
else:
    print("Usando cadena default.")



try: 
    print("Conectando a base de datos...")
    conexion = pyodbc.connect(cadena_conexion)
    print(conexion)
    cursor = conexion.cursor()

except Exception as e: 
    print("No fue posible conectar a la base de datos.")
    time.sleep(6)


def doAvanceTotal():

    print("Estoy en avance total...")

    #ordenamiento = "ORDER BY " + campo + " " + orden

    query = queries.totalNoRuteadas
    cursor.execute(query)
    filas = cursor.fetchmany(1000)

    print("FILAS: ", filas)

    data_global = {}
    
    totales_data = []

    for fila in filas:

        row_data = {
            "GuiaId": fila[0],
            "ClienteId": fila[1],
            "LocationType": fila[2],
            "Latitud": fila[3],
            "Longitud": fila[4],
            "TipoMovimientoOperativoId": fila[5],
            "TipoCodigoPostal": fila[6]
        }

        totales_data.append(row_data)
    
    data_global["GUIAS"] = totales_data

    print("Entrega Final:")
    print(data_global)

    return data_global

