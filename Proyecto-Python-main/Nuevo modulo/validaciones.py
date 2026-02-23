def validar_id_unico(id_buscar, lista_datos):
    """
    Verifica que un ID no exista ya en la lista
    Uso básico de for in
    """
    for elemento in lista_datos:
        if elemento['id'] == id_buscar:
            return False  # ID ya existe
    return True  # ID disponible

def validar_numero_positivo(texto):
    """
    Valida que un texto sea un número positivo
    Uso básico de for in
    """
    if texto == "" or texto == "0":
        return False
    
    for caracter in texto:
        if caracter not in '0123456789':
            return False
    
    return True