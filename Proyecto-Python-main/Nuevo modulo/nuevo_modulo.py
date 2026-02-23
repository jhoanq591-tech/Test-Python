from fecha import obtener_fecha_hora_manual
from validaciones import validar_id_unico, validar_numero_positivo
from jsones import cargar_reparacion, guardar_reparacion

def registrar_reparaciones(reparaciones):
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 10 + " Registrar Reparaciones" + " " * 11 + "║")
    print("╚" + "═" * 50 + "╝\n")

    reparaciones = cargar_reparacion("reparaciones.json")
    # Validar ID
    while True:
        id = input(" ID de la herramienta (ej: H001): ").strip()
        
        if id == "":
            print("❌ El ID no puede estar vacío")
            continue
        
        if not validar_id_unico(id, reparaciones):
            print("❌ Error: Ya existe una herramienta con ese ID")
            continue
        
        break

    # Validar nombre
    while True:
        nombre = input(" Nombre de la herramienta: ").strip()
        if nombre == "":
            print("❌ El nombre no puede estar vacío")
            continue
        break

    # Validar categoría
    while True:
        categoria = input(" Categoría (ej: Eléctrica, Manual, Jardín): ").strip()
        if categoria == "":
            print("❌ La categoría no puede estar vacía")
            continue
        break

    # Validar cantidad
    while True:
        cantidad = input(" Cantidad disponible: ").strip()
        if validar_numero_positivo(cantidad):
            break
        else:
            print("❌ Debe ingresar un número positivo válido")

    # Validar estado
    print("\n Estados disponibles:")
    print("  1. Nuevo")
    print("  2. Usado")
    print("  3. Dañado")
    print("  4. Reparacion")
    
    while True:
        estado_opcion = input("Seleccione el estado (1, 2 o 3): ").strip()
        if estado_opcion == "1":
            estado = "Nuevo"
            break
        elif estado_opcion == "2":
            estado = "Usado"
            break
        elif estado_opcion == "3":
            estado = "Dañado"
            break
        elif estado_opcion == "4":
            estado = "Reparacion"
        else:
            print("❌ Opción inválida. Ingrese 1, 2 o 3")
        
        fecha_de_inicio = obtener_fecha_hora_manual()

    # Validar ubicación
    while True:
        ubicacion = input("📍 Ubicación de almacenamiento: ").strip()
        if ubicacion == "":
            print("❌ La ubicación no puede estar vacía")
            continue
        break

    nueva_reparacion = {
        "id_de_herramienta": id,
        "nombre": nombre,
        "estado": estado,
        "fecha_de_inicio": fecha_de_inicio,
        "fecha_estimada_fin": estado,
        "observacaiones": ubicacion
    }

    reparaciones.append(nueva_reparacion)
    guardar_reparacion("reparaciones.json", reparaciones)
    print("\n✅ ¡Herramienta agregada correctamente!")
    input("Presione cualquier letra.")

def most_reparaciones(reparaciones):
    """Muestra todas las herramientas registradas usando for in"""
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 12 + " LISTA DE HERRAMIENTAS" + " " * 13 + "║")
    print("╚" + "═" * 50 + "╝\n")
    
    if not reparaciones:
        print("⚠️  No hay herramientas registradas.\n")
        return
    
    contador = 1
    for reparacion in reparaciones:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"Herramienta #{contador}")
        print(f"   ID:        {reparacion['id']}")
        print(f"   Nombre:    {reparacion['nombre']}")
        print(f"   Categoría: {reparacion['categoria']}")
        print(f"   Cantidad:  {reparacion['cantidad']}")
        print(f"   Estado:    {reparacion['estado']}")
        print(f"   Ubicación: {reparacion['ubicacion']}")
        contador = contador + 1
    
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print(f" Total de herramientas: {len(reparaciones)}")

def menu():
    print("""
Menu herramientas
1. mostrar herramientas
2. registrar reparaciones
3. salir
""")
    
def nuevo_main():
    menu()
    reparaciones = cargar_reparacion("reparaciones.json")
    while True:
        opcion = input("Ingrese un numero del 1 al 3:")
        if opcion == "1":
            most_reparaciones(reparaciones)
        elif opcion == "2":
            registrar_reparaciones(reparaciones)
        elif opcion == "3":
            print("Adios.")
            break
        else:
            input("Presione cualquier letra")

nuevo_main()