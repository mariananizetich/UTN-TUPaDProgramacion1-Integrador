from lectura_escritura import obtener_base_paises
from validaciones import existe_nombre, esta_vacio

def buscar_pais():
    paises = obtener_base_paises()
    
    if not paises:
        print ("El listado de países está vacío.")
        return
   
    nombre = input("Ingrese el nombre del país a buscar: ").strip()
    pais_encontrado= False
    
    while True:
    
        if esta_vacio(nombre):
            print ("El nombre del país ingresado NO existe o está vacío.")
            
            resp = input("Deseas ingresarlo nuevamente? (s: vuelve a ingresar / n: Regresa al menú anterior) ")

            if resp.lower().strip() == "s":
                nombre = input("Ingrese nuevamente el país: ").strip()
                continue
            else: break
            
        else: 
            for pais in paises:
                if pais["nombre"].lower() == nombre.lower():
                    print(f" País: {pais["nombre"]}\n Población: {pais["poblacion"]}\n Superficie: {pais["superficie"]}\n Continente: {pais["continente"]}")
                    pais_encontrado=True
                    return

                #verifico si el nombre de pais ingresado esta contenido en alguno de los paises de mi lista
                elif nombre.lower() in pais["nombre"].lower():
                    coincidencia = pais["nombre"].lower()
                    print(f"Intentaste filtrar: {coincidencia}. El detalle es el siguiente: ")
                    print(f" País: {pais["nombre"]}\n Población: {pais["poblacion"]}\n Superficie: {pais["superficie"]}\n Continente: {pais["continente"]}")
                    pais_encontrado=True
                    return
                
            if not pais_encontrado:
                print("No se encuentra el país ingresado.")
                resp = input("¿Deseas ingresarlo nuevamente? (s: vuelve a ingresar / n: Regresa al menú anterior) ")

                if resp.lower().strip() == "s":
                    nombre = input("Ingrese nuevamente el país: ").strip()
                    continue
                else: break

        
