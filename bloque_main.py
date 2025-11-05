from datos import agregar_pais, actualizar_poblacion_superficie
from busquedas import buscar_pais
from filtro import filtrar_paises

def  mostrar_menu():
    while True:
        
        print("=" * 50)
        print(" MENU DE PAISES")
        print("-" * 50)
        print("1. Agregar pais") 
        print("2. Actualizar poblacion y superficie") 
        print("3. Buscar pais") 
        print("4. Filtrar paises") 
        print("5. Ordenar paises")
        print("6. Mostrar estadisticas") 
        print("7. Salir")
        print("-" * 50)

        opcion= input ("Seleccione opcion: (1-7):  ").strip()
        
        match opcion:
            case "1": agregar_pais()
            case "2": actualizar_poblacion_superficie()
            case "3": buscar_pais()
            case "4": filtrar_paises()
            case "5": pass
            case "6": pass
            case "7": break
            case _: print ("Opcion incorrecta. Ingrese una opcion valida")

# --------------------------------- Llamada a la funcion menu ---------------------------------

mostrar_menu()