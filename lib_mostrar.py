def mostrar_pelicula(pelicula) -> None:
    """Muestra las peliculas por aatributo

    Args:
        pelicula (dict): diccionario de pelicula
    """
    print(
        f"{pelicula['id']:3}| "
        f"{pelicula['titulo']:29}| "
        f"{pelicula['genero']:15}| "
        f"{pelicula['rating']:6}|"
    )

def mostrar_peliculas(lista):
    
    print("ID   TITULO                     GENERO         RATING ")
    for pelicula in lista:
        mostrar_pelicula(pelicula)        
        

def mostrar_titulo_rating(lista,clave_uno,clave_dos):
    print("---------------------------------")
    print(f"{clave_uno}                  {clave_dos}")
    print("---------------------------------")
    
    for elemento in lista:
        print(f" {elemento[clave_uno]:15}   {elemento[clave_dos]}")    
        
def mostrar_mensaje(mensaje):
    print(mensaje)