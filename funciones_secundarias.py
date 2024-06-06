from random import randint
def asignar_rating(i, max=10, min=1):
    """asigna un valor random

    Args:
        i (dict): diccionario de la lista
        max (int): numero maximo
        min (int): numero minimo
    """
    i["rating"] = randint(min, max)
def asignar_genero(i, max=4, min=1):
    """asigna un valor random

    Args:
        i (dict): diccionario de la lista
        max (int): numero maximo
        min (int): numero minimo
    """
    codigo_genero = randint(min, max)
    if codigo_genero == 1:
        i["genero"] = "drama"
    elif codigo_genero == 2:
        i["genero"] = "comedia"
    elif codigo_genero == 3:
        i["genero"] = "accion"
    else:
        i["genero"] = "terror"




def mapper(lista, funcion):
    """recorre una lista y realiza una funcion a cada elemento

    Args:
        lista (list): lista de diccionarios de peliculas
        funcion (funcion): funcion a realizar en cada elemento
    """
    for pelicula in lista:
        funcion(pelicula)


def calcular_maximo_dos(lista, atributo):
    """Calcula los  maximos de determinado atributo dentro de una lista de diccionarios

    Args:
        lista (list):lista de heroes
        atributo (str): la clave del diccionario de la que se quiere sacar el maximo

    Returns:
        list: retorna una lista de diccionarios que contiene los heroes del maximo en determinado atributo
    """
    bandera = True
    numero_maximo = None
    pelicula_max_rating = []
    for i in lista:
        if  (bandera ==True)or(int(i[atributo]) >(numero_maximo)) :
            
            numero_maximo =int(i[atributo])
            bandera= False
    
    for i in lista:
        if int(i[atributo])== numero_maximo:
            pelicula_max_rating.append(i)
    return pelicula_max_rating

