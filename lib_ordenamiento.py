def ordenar_dos_criterios(lista:list, key_uno, key_dos):
    """ Ordena una lista de diccionarios por dos criterios

    Args:
        lista  (list): lista de diccionarios
        key_uno(str): clave del primer criterio(Marca)
        key_dos(str): clave del segundo criterio (Precio)

    Returns:
        _type_: _description_
    """
    tam = len(lista)   
    for i in range(0,tam - 1):    
       for j in range(i+1,tam):  
        if  (lista[i][key_uno] > lista[j][key_uno]) or (lista[i][key_uno] == lista[j][key_uno] and lista[i][key_dos]<lista[j][key_dos]): 
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
    