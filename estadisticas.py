from lectura_escritura import obtener_base_paises
from statistics import mean


# Funciones para obtener valores del listado
def por_poblacion(pais):
    return pais["poblacion"]



def mostrar_estadisticas():
    # Se obtiene el listado de países
    paises = obtener_base_paises()
    
    # Se comprueba que no esté vacío
    if not paises:
        print ("El listado de países está vacío.")
        return
    

    # País con mayor población
    mayor_poblacion = max(paises, key=por_poblacion)

    # País con menor población
    menor_poblacion = min(paises, key=por_poblacion)

    # Promedio de población

    # Se crea una lista con la población de cada país
    poblaciones = [pais["poblacion"] for pais in paises]
    # Se calcula el promedio
    promedio_poblacion = round(mean(poblaciones), 2)
 
    
    # Promedio de superficie

    # Se crea una lista con la superficie de cada país
    superficies = [pais["superficie"] for pais in paises]
    # Se calcula el promedio
    promedio_superficie = round(mean(superficies), 2)

    # Cantidad de países por continente

    # Se inician contadores en 0 para cada continente
    americano = 0
    africano = 0
    asiatico = 0
    europeo = 0
    oceania = 0

    # Se recorre la lista de países para obtener cada continente
    for pais in paises:
        continente = pais["continente"].strip()

        # Se suman las cantidades de países en cada continente
        if continente == "Americano":
            americano += 1
        elif continente == "Africano":
            africano += 1
        elif continente == "Asiatico":
            asiatico += 1
        elif continente == "Europeo":
            europeo += 1
        elif continente == "Oceania":
            oceania +=1

    # Se muestran resultados por pantalla
    print("\n····· ESTADÍSTICAS ·····\n")

    print(f"País con mayor población: {mayor_poblacion['nombre']} con {mayor_poblacion['poblacion']} habitantes.")
    print(f"País con menor población: {menor_poblacion['nombre']} con {menor_poblacion['poblacion']} habitantes.")
    print("·" * 20)

    print(f"Promedio de población: {promedio_poblacion}")
    print(f"Promedio de superficie: {promedio_superficie}")
    print("·" * 20)

    print("Países por continente:")

    print(f"América: {americano} países.")
    print(f"África: {africano} países.")
    print(f"Asia: {asiatico} países.")
    print(f"Europa: {europeo} países.")
    print(f"Oceanía: {oceania} países.")




