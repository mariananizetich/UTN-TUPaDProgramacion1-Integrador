from validaciones import existe_nombre, esta_vacio, validar_cantidad
from lectura_escritura import obtener_base_paises, agregar_a_base_paises, guardarTodosLosPaises
    
# ---------------------------------------- Funcion agregar pais -------------------------   
def agregar_pais():
    print("·········· AGREGAR NUEVO PAÍS ··········")
    nombre_pais = input("Ingrese nombre de país: ").strip()

    while True:
        if esta_vacio(nombre_pais) or existe_nombre(nombre_pais):
            print("El nombre del país no puede estar vacío o ya existe.")
            nombre_pais = input("Ingrese nuevamente nombre de país: ").strip()
        else: break
    
    poblacion = input("Ingrese cantidad de población: ").strip()
    
    while True:
        if not validar_cantidad(poblacion):
            print ("La cantidad ingresada es incorrecta.")
            poblacion = input("Ingrese cantidad de población: ").strip()
        else: break
        
    poblacion = int(poblacion)
    
    superficie = input("Ingrese superficie en km2: ").strip()
    
    while True:
        if not validar_cantidad(superficie):
            print ("La cantidad ingresada es incorrecta.")
            superficie = input("Ingrese superficie en km2: ").strip()
        else: break
        
    superficie = int(superficie)
    
    continente = input("Ingrese continente: ").strip()

    while True:
        if esta_vacio(continente):
            print("El continente no puede estar vacío.")
            continente = input("Ingrese continente: ").strip()
        else: break
    
    
    agregar_a_base_paises({"nombre": nombre_pais , "poblacion": poblacion, "superficie": superficie, "continente": continente})
    
    print("PAÍS AGREGADO CORRECTAMENTE")

# ------------------------- Funcion para actualizar poblacion y superficie -------------------------

def actualizar_poblacion_superficie():

    paises = obtener_base_paises()
    
    if not paises:
        print ("El listado de países esta vacío.")
        return
        
    nombre = input("Ingrese el nombre del país a modificar: ").strip()
    while True:
    
        if not existe_nombre(nombre) or esta_vacio(nombre):
            print ("El nombre del país ingresado NO existe o esta vacío.")
            resp = input("Deseas ingresarlo nuevamente? (s: vuelve a ingresar / n: Regresa al menú anterior) ")

            if resp.lower().strip() == "s":
                nombre = input("Ingrese el nombre del país a modificar: ").strip()
                continue
            else: break
            
        else: break

    for pais in paises:
        if pais["nombre"].lower().strip() == nombre.lower():
            
            print("·" * 10)
            print("A. Actualizar población")
            print("B. Actualizar superficie") 
            print("Presiona cualquier tecla para volver al menú anterior")
            print("·" * 10)

            opcion= input ("Seleccione opción: (A-B):  ").strip().upper()
        
            match opcion:
                case "A": # --------------------- actualiza poblacion ------------------
                    poblacion = input("Actualiza la cantidad de población: ").strip()

                    while True:
                        if not validar_cantidad(poblacion):
                            print ("La cantidad ingresada es incorrecta.")
                            poblacion = input("Actualiza la cantidad de población: ").strip()
                        else: break
                        
                    pais["poblacion"] = poblacion

                    guardarTodosLosPaises(paises)

                    print("Actualización realizada con éxito.")
                    break

                case "B": # --------------------- actualiza superficie ------------------
                    
                    superficie = input("Actualiza la superficie: ").strip()

                    while True:
                        if not validar_cantidad(superficie):
                            print ("La cantidad ingresada es incorrecta.")
                            superficie = input("Actualiza la superficie: ").strip()
                        else: break
                        
                    pais["superficie"] = superficie

                    guardarTodosLosPaises(paises)

                    print("Actualización realizada con éxito.")
                    break
                
                case _: break
            
            
            
                
                
           