import json
from openpyxl import Workbook

def leer_datos_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return None

def escribir_datos_en_archivo(datos, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo)

def escribir_datos_en_excel(datos, nombre_archivo):
    libro_trabajo = Workbook()
    hoja = libro_trabajo.active

    for fila in datos:
        hoja.append(fila)

    libro_trabajo.save(nombre_archivo)
