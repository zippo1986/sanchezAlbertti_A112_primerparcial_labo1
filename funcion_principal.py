"""Enunciado:
Se dispone de un archivo con datos acerca de películas, que tiene el siguiente formato:
id_peli, titulo, genero, rating
por ejemplo: 1,Adventures of Rocky,sin genero,0
2,My Brother the Devil,sin genero,0
3,Criminal,sin genero,0
Se deberá realizar un programa que permita el análisis de dicho archivo y sea capaz de generar
nuevos archivos de salida de formato similar filtrados por varios criterios:
el programa contará con el siguiente menú:
1) Cargar archivo .CSV: Se pedirá el nombre del archivo y se cargará en una lista de
diccionarios los elementos
del mismo.
2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de las películas.
3) Asignar rating: Se deberá hacer uso de la función map. La cual recibirá la lista y una
función que asignará a la película un valor de rating flotante entre 1 y 10 con 1 decimal
calculado de manera aleatoria se mostrará por pantalla el mismo.
4) Asignar género: Se deberá hacer uso de la función map. La cual recibirá la lista y una
función que asignará a la película un género de acuerdo a un número aleatorio entre 1 y 4.
1: drama
2: comedia
3: acción
4: terror
5) Filtrar por género: Se deberá pedir un género y escribir un archivo igual al original, pero
donde solo
aparezcan películas del género seleccionado. El nombre del archivo será p.e. comedias.csv
6) Ordenar películas: Se deberá mostrar por pantalla un listado de las películas ordenadas por
género y dentro de las del mismo género que aparezcan ordenadas por rating descendente.
7) Informar Mejor Rating: Mostrar el titulo y el rating de la película con más rating
8) Guardar películas: Se deberá guardar el listado del punto anterior en un archivo JSON.
9) Salir.

Requerimientos del desarrollo.
Nota 1: Todas las funciones deben estar en un módulo distinto al programa principal
y respetar las reglas de estilo de la cátedra.
Nota 2: Todas las funciones deben tener su propio docstring
Nota 3: Para ordenar se deberá utilizar los algoritmos de ordenamiento vistos en la catedra"""

from lib_validaciones import *
from lib_archivos import *
from lib_mostrar import *
from funciones_secundarias import *
from lib_filtrado import *
from lib_ordenamiento import *
import sys
def main ():
    
    bandera_carga = False
    bandera_rating = False
    bandera_genero = False
    bandera_peliculas_max_rat = False
    lista_peliculas= []
    peliculas_max_rating = []
    confirmacion = "s"
    while confirmacion == "s":
        mostrar_mensaje("""Menu de opciones
                    1)cargar archivo
                    2)imprimir lista
                    3) Asignar Rating
                    4)Asignar genero
                    5)filtrar por genero
                    6)ordenar peliculas
                    7)informar mejor rating
                    8) guardar peliculas
                    9)Exit""")
        
        opcion = input("Ingrese opcion")
        while not validar_entero(opcion):
            opcion= input("Ingrese opcion")
        match (opcion):
            case "1":
                lista_peliculas= csv_a_list("movies.csv")
                bandera_carga = True
            
            case "2":
                if not bandera_carga:
                    mostrar_mensaje("No se puede mostrar la lista sin cargarla primero")
                else:
                    mostrar_peliculas(lista_peliculas)
            
            case "3":
                if not bandera_carga:
                    mostrar_mensaje("No se puede asignar ratings  sin cargar la lista primero")
                else:
                    mapper(lista_peliculas,asignar_rating)
                    mostrar_peliculas(lista_peliculas)
            case "4":
                if not bandera_carga:
                    mostrar_mensaje("No se puede asignar genero sin cargar la lista primero")
                else:
                    mapper(lista_peliculas,asignar_genero)
                    mostrar_peliculas(lista_peliculas)
                    bandera_genero = True
            case "5":
                if not bandera_genero:
                    mostrar_mensaje("No se puede listar y guardar las comedias sin asignar genero")
                else:
                    lista_comedias = filtrar_datos(lista_peliculas, "comedia", "genero")
                    guardar_csv_dos("comedias.csv",lista_comedias)
            case "6":
                if not bandera_genero and bandera_rating:
                    mostrar_mensaje("No se puede realizare el ordenamiento sin asignar genero y rating")
                    
                else:
                    ordenar_dos_criterios(lista_peliculas,"genero","rating")
                    mostrar_peliculas(lista_peliculas)
                    
            case "7":
                if bandera_rating:
                    peliculas_max_rating = calcular_maximo_dos(lista_peliculas,"rating")
                    mostrar_titulo_rating(peliculas_max_rating,"titulo","rating")
                    bandera_peliculas_max_rat= True
                else:
                    mostrar_mensaje("No se puede realizar la operacion sin cargar el rating")
            case "8":
                if bandera_peliculas_max_rat:
                    guardar_json_rating(peliculas_max_rating, "peliculas_max_rat.json")
                else:mostrar_mensaje("no se puede guardar el archivo sin realizar la operacion anterior")
            case "9":
                sys.exit()
                
                
                
                
        
        confirmacion = input("desea realizar otra operacion?")