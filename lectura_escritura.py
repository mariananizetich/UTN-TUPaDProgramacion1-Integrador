import csv
import os

NOMBRE_ARCHIVO = "base_de_paises.csv"

# ---------------------------------------- agregar datos al csv "a" -------------------------
def agregar_a_base_paises(pais):
  
  with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
    escritor.writerow(pais)

# ---------------------------------------- crea archivo vacio/ lee archivo -------------------------

def obtener_base_paises():
    base = []
    
    # Si el archivo no existe, lo crea con encabezado vacío
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            escritor.writeheader()
            print("-Base de paises iniciada-")
            return base 
    
    # Lectura del archivo existente
    with open (NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            base.append({"nombre": fila["nombre"], "poblacion": int(fila["poblacion"]), "superficie": int(fila["superficie"]), "continente": fila["continente"]})
            
    return base

# ---------------------------------------- Esccribe de nuevo "w" -------------------------
def guardarTodosLosPaises(paises):
  with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
    escritor.writeheader()
    escritor.writerows(paises)