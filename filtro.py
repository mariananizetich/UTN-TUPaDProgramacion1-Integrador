from lectura_escritura import obtener_base_paises, guardarTodosLosPaises
from validaciones import existe_nombre, esta_vacio, validar_cantidad, existe_continente

def filtrar_paises():

    paises = obtener_base_paises()
    
    if not paises:
        print ("El listado de paises esta vacio")
        return
    
    while True: 
        print("·····FILTRAR PAISES·····" )
        print("A. Por continente")
        print("B. Por rango de población") 
        print("c. Por rango de superficie") 
        print("Presiona cualquier tecla para volver al menu anterior")
        print("·" * 20)

        opcion= input ("Seleccione opcion: (A-B-C):  ").strip().upper()
            
        match opcion:
            case "A":
                continente = input("Ingresa continente a filtrar: ").strip().lower()

                while True:
                    if not existe_continente(continente) or esta_vacio (continente):
                        print ("El continente ingresado no existe o esta vacio")
                        resp = input("Deseas ingresarlo nuevamente? (s: vuelve a ingresar / n: Regresa al menu anterior) ")

                        if resp.lower().strip() == "s":
                            continente = input("Ingresa continente a filtrar: ").strip().lower()
                            continue
                        else: break
                    else: break
                
                for pais in paises:
                    if pais["continente"].lower().strip() == continente:
                        print(f" Pais: {pais["nombre"]}\n Poblacion: {pais["poblacion"]}\n Superficie: {pais["superficie"]}\n Continente: {pais["continente"]}")
                        print(".....")
                        
            
            case "B": 
                print ("___RANGO DE POBLACION___")
                print("A. 0 a 20 millones de personas") 
                print("B. Entre 20 millones y 40 millones de personas") 
                print("C. Mas de 40 millones") 
                print("Ingresa otra opcion para volver al menu anterior\n") 
                
                rango = input("Selecciona rango de poblacion a filtrar: ").upper()
                rango_encontrado= False
                
                for pais in paises:
                    if rango == "A":
                        if pais["poblacion"] <= 20000000:
                            print(f" Pais: {pais["nombre"]}\n Poblacion: {pais["poblacion"]}\n Superficie: {pais["superficie"]}\n Continente: {pais["continente"]}")
                            print("________________\n")
                            rango_encontrado= True
                           
                    elif rango == "B":
                        if pais["poblacion"] > 20000000 and pais["poblacion"] < 40000000 :
                            print(f" Pais: {pais["nombre"]}\n Poblacion: {pais["poblacion"]}\n Superficie: {pais["superficie"]}\n Continente: {pais["continente"]}")
                            print("________________\n")
                            rango_encontrado= True
                           
                    elif rango == "C":
                        if pais["poblacion"] >= 40000000 :
                            print(f" Pais: {pais["nombre"]}\n Poblacion: {pais["poblacion"]}\n Superficie: {pais["superficie"]}\n Continente: {pais["continente"]}")
                            print("________________\n")
                            rango_encontrado= True
                            
                if not rango_encontrado:
                    print("No hay países con población dentro del rango seleccionado")
                    
            case "C": 
                print ("___RANGO DE SUPERFICIE___")
                print("A. 0 a 500.000 km2") 
                print("B. Entre 500.000 a 4.000.000 km2") 
                print("C. Mas de 4.000.000 km2") 
                print("Ingresa otra opcion para volver al menu anterior") 
                
                rango = input("Selecciona rango de superficie a filtrar: ").upper()
                rango_encontrado= False
                
                for pais in paises:
                    if rango == "A":
                        if pais["superficie"] <= 500000:
                            print(f" Pais: {pais["nombre"]}\n Poblacion: {pais["poblacion"]}\n Superficie: {pais["superficie"]}\n Continente: {pais["continente"]}")
                            print("________________\n")
                            rango_encontrado= True
                            
                    elif rango == "B":
                        if pais["superficie"] > 500000 and pais["superficie"] < 4000000 :
                            print(f" Pais: {pais["nombre"]}\n Poblacion: {pais["poblacion"]}\n Superficie: {pais["superficie"]}\n Continente: {pais["continente"]}")
                            print("________________\n")
                            rango_encontrado= True
                            
                    elif rango == "C":
                        if pais["superficie"] >= 4000000 :
                            print(f" Pais: {pais["nombre"]}\n Poblacion: {pais["poblacion"]}\n Superficie: {pais["superficie"]}\n Continente: {pais["continente"]}")
                            print("________________\n")
                            rango_encontrado= True
                            
                if not rango_encontrado:
                    print("No hay países con superficie dentro del rango seleccionado")
                    
            case _: break
                