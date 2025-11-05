from datos import agregar_pais, actualizar_poblacion_superficie
from busquedas import buscar_pais
from filtro import filtrar_paises
from ordenamiento import ordenar_paises
from estadisticas import mostrar_estadisticas

def  mostrar_menu():
    while True:
        
        print("=" * 50)
        print(" MENÚ DE PAÍSES")
        print("-" * 50)
        print("1. Agregar país") 
        print("2. Actualizar población y superficie") 
        print("3. Buscar país") 
        print("4. Filtrar países") 
        print("5. Ordenar países")
        print("6. Mostrar estadísticas") 
        print("7. Salir")
        print("-" * 50)

        opcion= input ("Seleccione opción: (1-7):  ").strip()
        
        match opcion:
            case "1": agregar_pais()
            case "2": actualizar_poblacion_superficie()
            case "3": buscar_pais()
            case "4": filtrar_paises()
            case "5": ordenar_paises()
            case "6": mostrar_estadisticas()
            case "7": break
            case _: print ("Opción incorrecta. Ingrese una opción válida.")

# --------------------------------- Llamada a la funcion menú ---------------------------------

mostrar_menu()