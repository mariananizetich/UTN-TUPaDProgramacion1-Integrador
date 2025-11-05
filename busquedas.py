from lectura_escritura import obtener_base_paises
from validaciones import existe_nombre, esta_vacio

def buscar_pais():
    paises = obtener_base_paises()
    
    if not paises:
        print ("El listado de paises esta vacio")
        return
   
    nombre = input("Ingrese el nombre del pais a buscar: ").strip()
    pais_encontrado= False
    
    while True:
    
        if esta_vacio(nombre):
            print ("El nombre del pais ingresado NO existe o esta vacio.")
            
            resp = input("Deseas ingresarlo nuevamente? (s: vuelve a ingresar / n: Regresa al menu anterior) ")

            if resp.lower().strip() == "s":
                nombre = input("Ingrese nuevamente el pais: ").strip()
                continue
            else: break
            
        else: 
            for pais in paises:
                if pais["nombre"].lower() == nombre.lower():
                    print(f" Pais: {pais["nombre"]}\n Poblacion: {pais["poblacion"]}\n Superficie: {pais["superficie"]}\n Continente: {pais["continente"]}")
                    pais_encontrado=True
                    return

                #verifico si el nombre de pais ingresado esta contenido en alguno de los paises de mi lista
                elif nombre.lower() in pais["nombre"].lower():
                    coincidencia = pais["nombre"].lower()
                    print(f"Intentaste filtrar: {coincidencia}. El detalle es el siguiente: ")
                    print(f" Pais: {pais["nombre"]}\n Poblacion: {pais["poblacion"]}\n Superficie: {pais["superficie"]}\n Continente: {pais["continente"]}")
                    pais_encontrado=True
                    return
                
            if not pais_encontrado:
                print("No se encuentra el pais ingresado")
                resp = input("Deseas ingresarlo nuevamente? (s: vuelve a ingresar / n: Regresa al menu anterior) ")

                if resp.lower().strip() == "s":
                    nombre = input("Ingrese nuevamente el pais: ").strip()
                    continue
                else: break

        
