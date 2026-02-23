import json
import os

CARPETA_BASE = os.path.dirname(os.path.abspath(__file__))

def cargar_reparacion(archivo="reparaciones.json"):
    ruta_completa = os.path.join(CARPETA_BASE, archivo)
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️ ERROR: No se encontró el archivo {archivo} en {CARPETA_BASE}")
        return []
    except json.JSONDecodeError:
        print(f"⚠️ ERROR: El archivo {archivo} tiene formato JSON inválido")
        return []

def guardar_reparacion(archivo, datos):
    ruta_completa = os.path.join(CARPETA_BASE, archivo)
    with open(ruta_completa, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
