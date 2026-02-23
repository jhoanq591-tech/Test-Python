def validar_fecha(fecha):
    """
    Valida que una fecha tenga formato DD/MM/AAAA y sea válida
    Usa for in para validar caracteres
    """
    # Verificar longitud
    if len(fecha) != 10:
        return False
    
    # Verificar formato con /
    if fecha[2] != '/' or fecha[5] != '/':
        return False
    
    # Extraer día, mes, año
    dia_str = ""
    mes_str = ""
    anio_str = ""
    
    # Extraer día (posiciones 0-1)
    for i in range(2):
        if fecha[i] not in '0123456789':
            return False
        dia_str = dia_str + fecha[i]
    
    # Extraer mes (posiciones 3-4)
    for i in range(3, 5):
        if fecha[i] not in '0123456789':
            return False
        mes_str = mes_str + fecha[i]
    
    # Extraer año (posiciones 6-9)
    for i in range(6, 10):
        if fecha[i] not in '0123456789':
            return False
        anio_str = anio_str + fecha[i]
    
    # Convertir a números
    dia = int(dia_str)
    mes = int(mes_str)
    anio = int(anio_str)
    
    # Validar rangos
    if mes < 1 or mes > 12:
        return False
    
    if dia < 1 or dia > 31:
        return False
    
    if anio < 2000 or anio > 2100:
        return False
    
    # Validar días según mes
    if mes == 2:  # Febrero
        if dia > 29:
            return False
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:  # Meses de 30 días
        if dia > 30:
            return False
    
    return True

def validar_hora(hora):
    # Verificar longitud
    if len(hora) != 5:
        return False
    
    # Verificar formato con :
    if hora[2] != ':':
        return False
    
    # Extraer horas y minutos
    horas_str = ""
    minutos_str = ""
    
    # Extraer horas (posiciones 0-1)
    for i in range(2):
        if hora[i] not in '0123456789':
            return False
        horas_str = horas_str + hora[i]
    
    # Extraer minutos (posiciones 3-4)
    for i in range(3, 5):
        if hora[i] not in '0123456789':
            return False
        minutos_str = minutos_str + hora[i]
    
    # Convertir a números
    horas = int(horas_str)
    minutos = int(minutos_str)
    
    # Validar rangos
    if horas < 0 or horas > 23:
        return False
    
    if minutos < 0 or minutos > 59:
        return False
    
    return True

def obtener_fecha_hora_manual(hora):
    print("\n📅 Ingrese la fecha y hora actual:")
    
    # Validar fecha
    while True:
        fecha = input("Fecha (DD/MM/AAAA): ").strip()
        
        if validar_fecha(fecha):
            break
        else:
            print("❌ Fecha inválida. Use formato DD/MM/AAAA")
            print("   Ejemplo: 14/02/2024")
            print("   Día: 01-31, Mes: 01-12, Año: 2000-2100")
    
    # Validar hora
    while True:
        hora = input("Hora (HH:MM): ").strip()
        
        if validar_hora(hora):
            break
        else:
            print("❌ Hora inválida. Use formato HH:MM (24 horas)")
            print("   Ejemplo: 14:30")
            print("   Horas: 00-23, Minutos: 00-59")
    
    return f"{fecha} {hora}"