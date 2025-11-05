from lectura_escritura import obtener_base_paises
from validaciones import esta_vacio

# Funciones para obtener valores del listado
def por_nombre(pais):
    return pais["nombre"].strip().lower()
def por_poblacion(pais):
    return pais["poblacion"]
def por_superficie(pais):
    return pais["superficie"]

# Función para ordenar países
def ordenar_paises():

    # Se obtiene el listado de países
    paises = obtener_base_paises()

    # Se comprueba que el listado no esté vacío
    if not paises:
        print ("El listado de países está vacío.")
        return

    # Menú de opciones
    while True:
        print("·····ORDENAR PAÍSES·····")
        print("A. Por nombre (A-Z).")
        print("B. Por población.")
        print("C. Por superficie (ascendente/descendente).")
        print("Presiona cualquier tecla para volver al menú anterior.")
        print("·" * 20)

        # Se solicita una opción al usuario
        opcion = input("Seleccione opción: (A-B-C): ").strip().upper()

        # Interacción
        match opcion:
            case "A":
                print("\n__PAÍSES POR ORDEN ALFABÉTICO__\n")

                # Se ordenan los países por orden alfabético
                paises_ordenados = sorted(paises, key=por_nombre)
                # Se muestran por pantalla
                for pais in paises_ordenados:
                     print(f"País: {pais['nombre']}\n Población: {pais['poblacion']}\n Superficie: {pais['superficie']} km2\n Continente: {pais['continente']}")
                     print(".....")
            case "B":
                print("\n__PAÍSES POR POBLACIÓN (MAYOR A MENOR)__\n")
                
                # Se ordenan los países por población, orden descendente
                paises_ordenados = sorted(paises, key=por_poblacion, reverse=True)
                # Se muestran por pantalla
                for pais in paises_ordenados:
                     print(f"País: {pais['nombre']}\n Población: {pais['poblacion']}\n Superficie: {pais['superficie']} km2\n Continente: {pais['continente']}")
                     print(".....")

            case "C":
                print("\n__PAÍSES POR SUPERFICIE__\n")

                while True:
                    # Se soliicta al usuario el orden
                    orden = input("Indique el orden que desee: Ascendente (A) - Descendente (D): ").strip().upper()

                    # Se comprueba que la entrada no esté vacía
                    if esta_vacio(orden):   
                        print("La opción ingresada no es válida.")
                        resp = input("¿Deseas ingresarlo nuevamente? (s: vuelve a ingresar / n: Regresa al menú anterior)").strip().lower()
                        if resp == "s":
                            continue
                        else: 
                            break

                    # Orden ascendente
                    if orden == "A":
                        paises_ordenados = sorted(paises, key=por_superficie)
                    
                    # Orden descendente
                    elif orden == "D":
                        paises_ordenados = sorted(paises, key=por_superficie, reverse=True)
                    
                    # Opción inválida
                    else:
                        resp = input("¿Deseas ingresarlo nuevamente? (s: vuelve a ingresar / n: Regresa al menú anterior): ").strip().lower()
                        if resp == "s":
                            continue
                        else: 
                            break
                    
                    # Se muestra por pantalla
                    for pais in paises_ordenados:
                        print(f"País: {pais['nombre']}\n Población: {pais['poblacion']}\n Superficie: {pais['superficie']} km2\n")
                    break
            # Se regresa al menú anterior
            case _:
                break





