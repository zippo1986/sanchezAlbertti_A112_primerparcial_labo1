def validar_entero(numero:str):
    """_summary_
    Valida que el numero pasado por str sea enttero

    Args:
        numero (str): recibe un numero en str

    Returns:
        _type_: retorna true o false
    """
    for i in numero:
        try:
            int(i)
            return True
        except ValueError:
            return False