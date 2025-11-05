from lectura_escritura import obtener_base_paises

def existe_nombre(nombre):
    listado_paises = obtener_base_paises()
    
    for p in listado_paises:
        if p["nombre"].lower().strip() == nombre.strip().lower():
            return True
    
    return False


def validar_cantidad(cantidad):
    if cantidad.isdigit():
        return True
    else: return False
    
    
def esta_vacio(dato):
    if not dato:
        return True
 
def existe_continente(continente):
    listado_paises = obtener_base_paises()
    
    for p in listado_paises:
        if p["continente"].lower().strip() == continente.strip().lower():
            return True
    
    return False
