def funcion_hash(clave):
    return hash(clave) % 10 

def insertar(tabla, clave, valor):
    indice = funcion_hash(clave)
    tabla[indice] = valor

def buscar(tabla, clave):
    indice = funcion_hash(clave)
    if indice in tabla and tabla[indice] is not None:
        return tabla[indice]
    else:
        return None

tabla_hash = [None] * 10  
    
insertar(tabla_hash, "Juan", 25)
insertar(tabla_hash, "María", 30)
insertar(tabla_hash, "Pedro", 28)
insertar(tabla_hash, "Ana", 35)

nombre_buscado = "Pedro"
resultado = buscar(tabla_hash, nombre_buscado)

if resultado is not None:
    print(f"La edad de {nombre_buscado} es {resultado}.")
else:
    print(f"{nombre_buscado} no encontrado en la tabla hash.")
