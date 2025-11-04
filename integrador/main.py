print("TRABAJO PRÁCTICO INTEGRADOR - PROGRAMACIÓN I")

# Importación de módulos necesarios
import os

# Se obtiene la ruta del archivo paises.csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Se construye la ruta al archivo 'paises.csv' dentro de esa carpeta
ruta_archivo = os.path.join(BASE_DIR, "paises.csv")


# Se crea una Función para leer el archivo
def lectura_archivo():
    # Se comprueba que la ruta del archivo exista
    if not os.path.exists(ruta_archivo):
            print("No se encontró archivo existente.\n")
            return []
    
    # Se inicia una lista vacía que guardará el diccionario con los elementos del archivo
    paises = []

    # Se abre el archivo en modo 'r' para leerlo
    with open(ruta_archivo, "r") as archivo:
        # Ignorar el encabezado
        # Contador de linea
        linea_numero = 0
        # Se recorre línea por línea
        for linea in archivo:
            # Se incrementa el contador en cada línea
            linea_numero += 1
            # Saltear primera línea
            if linea_numero == 1:
                continue

            # Se eliminan los espacios y saltos de línea con strip()
            linea = linea.strip()
            # Se ignornan las líneas vacías
            if not linea:
                 continue
            # Se dividen los elementos por coma
            partes = linea.split(",")
             # Se obtiene el país sin espacios ni saltos de línea
            nombre = partes[0].strip()
            # Se obtienen  la población y superficie y se convierten en enteros
            poblacion = int(partes[1].strip())
            superficie = int(partes[2].strip())
            # Se obtiene el continente sin espacios ni saltos de línea
            continente = partes[3].strip()

            # Se crea un diccionario con los elementos de cada país
            pais = {
                 "nombre": nombre,
                 "poblacion": poblacion,
                 "superficie": superficie,
                 "continente": continente
            }

            # Se agrega el diccionario a la lista
            paises.append(pais)
        
        return paises
    
# Se llama a la función para que se ejecute
paises = lectura_archivo()

# Función para buscar país
def buscar_pais(paises, nombre):
    pais = pais.lower().strip()
    # Se recorre la lista buscando existencias
    for pais in paises:
        if pais["nombre"].lower().strip() == nombre:
            # Devuelve el diccionario del país si se encuentra, o None si no existe
            return nombre
    return None

# Función para comprobar país válido, que no exista en la lista
def comprobar_pais(paises):
    while True:
                # Se solicita al usuario que ingrese el país
                nombre_pais = input("Por favor, ingrese el nombre del país que desea agregar: ").title().strip()
                # Se comprueba que no esté vacío
                if nombre_pais == "":
                    # Se informa error
                    print("No es posible ingresar un nombre vacío. Por favor, vuelva a intentarlo.\n")
                    continue
                
                if buscar_pais(paises, nombre_pais) is not None:
                
                    continue
            
                # Se devuelve el nombre del país
                return nombre_pais
    

# Función para el menú principal
def menu_principal(paises):
     
     # Se inicia un bucle que se repetirá cuando la opción ingresada no sea válida
     while True:

        print("MENÚ PRINCIPAL\n")
     
        # Menú
        print("1. Agregar un país.")
        print("2. Actualizar población de un país")
        print("3. Actualizar superficie de un país.")
        print("4. Buscar país.")
        print("5. Filtrar países por rango de población/rango de superficie.")
        print("6. Ordenar países por nombre/población/superficie.")
        print("7. Mostrar estadísticas.")
        print("8.Salir.\n")

        # Se solicita la opción al usuario
        opcion = input("Ingrese la opción que desea realizar: ")

        # Match case para la interacción
        match opcion:
            # Agregar país
            case "1":
                print("1. Agregar un país\n")

                # Se solicita al usuario el nombre del país
                pais = input("Ingrese el nombre del país que desea agregar: ")

                

                

            # Actualizar población
            case "2":
                print("2. Actualizar población de un país\n")

            # Actualizar superficie
            case "3":
                print("3. Actualizar superficie de un país\n")

            # Buscar país
            case "4":
                print("4. Buscar país\n")

            # Filtrar países
            case "5":
                print("5. Filtrar países\n")
                while True:
                    print("1. Filtrar países por continente.")
                    print("2. Filtrar países por rango de población.")
                    print("3. Filtrar países por rango de superficie.")
                    print("4. Volver al menú principal.")

                    filtrar = input("Indique de qué modo quiere filtrar países: ")

                    match filtrar:
                        case "1":
                            print("Por continente.")
                        case "2":
                            print("Por rango de población.")
                        case "3":
                            print("Por rango de superficie.")
                        case "4":
                            # Se sale del bucle y regresa al menú principal
                            break
                        case _:
                            print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                            continue

            # Ordenar países
            case "6":
                print("6. Ordenar países\n")
                while True:
                    print("1. Ordenar países por nombre.")
                    print("2. Ordenar países por población.")
                    print("3. Ordenar países por superficie.")
                    print("4. Volver al menú principal.")

                    ordenar = input("Indique de qué modo quiere filtrar países: ")

                    match ordenar:
                        case "1":
                            print("Por nombre.")

                            
                        case "2":
                            print("Por población.")
                        case "3":
                            print("Por superficie.")
                        case "4":
                            # Se sale del bucle y regresa al menú principal
                            break
                        case _:
                            print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                            continue
                
            # Mostrar estadísticas
            case "7":
                print("7. Mostrar estadísticas\n")
                
            # Salida
            case "8":

                # Mensaje de despedida
                print("¡Gracias por su visita! ¡Hasta pronto!\n")
                break

            # Opción inválida
            case _:
                # Se informa error
                print("La opción ingresada no es válida. Por favor, vuelva a intentarlo.\n")
          
         
    
menu_principal(paises)