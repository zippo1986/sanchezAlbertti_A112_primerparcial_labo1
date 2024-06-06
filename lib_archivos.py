import csv
import json
from funciones_secundarias import *

def csv_a_list(archivo:str):
    


    lista_diccionarios = []

    
    with open(archivo, mode='r', newline='', encoding='utf-8') as archivo:
        
        lector_csv = csv.DictReader(archivo)
        
        
        for fila in lector_csv:
            lista_diccionarios.append(fila)
            
    return lista_diccionarios

def guardar_csv_dos(nombre_archivo, lista_diccionarios):
    nombres_campos = lista_diccionarios[0].keys()
    with open(nombre_archivo, "w", newline="") as archivo_csv:
    
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=nombres_campos)

    
        escritor_csv.writeheader()

        for diccionario in lista_diccionarios:
            escritor_csv.writerow(diccionario)

    print("Archivo CSV guardado correctamente.")
    
def agregar_campos_lista(insumos_json, pelicula):
    """Agrega un registro completo

    Args:
        insumos_json (list): lista de insumos 
        insumo (dict): diccionario
    """
    insumos_json.append({
            "titulo": pelicula["titulo"],
            "rating": pelicula["rating"],
            
            
        })
def guardar_json_rating(peliculas_max_rat:list, nombre_archivo):
    """
    recorre lista de diccionarios de insumos busca si en la  clave nombre se 
    encuentra "Disco duro" y si está, agrega el registro a una lista
    luego abre un archivo jsoon y escribe todos los registros que cumplan con la busqueda
    Args:
        insumos (list): Lista de diccionarios de insumos
    """
    insumos_json = []
    for pelicula in peliculas_max_rat:
        
            
        agregar_campos_lista(peliculas_max_rat, pelicula)
    with open(nombre_archivo, "w") as archivo:
        json.dump(insumos_json, archivo, indent=4)
    print("Se ha generado el archivo insumos.json correctamente.")

    
    