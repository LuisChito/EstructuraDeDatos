POSTRES = {}

def imprimir_ingredientes(postre):
    if postre in POSTRES:
        print(f"Ingredientes de {postre}: {POSTRES[postre]}")
    else:
        print(f"No se encontró el postre {postre}")

def insertar_ingredientes(postre, ingredientes):
    if postre in POSTRES:
        POSTRES[postre].extend(ingredientes)
        print(f"Ingredientes agregados a {postre}: {POSTRES[postre]}")
    else:
        print(f"No se encontró el postre {postre}")

def eliminar_ingredientes(postre, ingredientes):
    if postre in POSTRES:
        for ingrediente in ingredientes:
            if ingrediente in POSTRES[postre]:
                POSTRES[postre].remove(ingrediente)
        print(f"Ingredientes eliminados de {postre}: {POSTRES[postre]}")
    else:
        print(f"No se encontró el postre {postre}")

def alta_postre(postre, ingredientes):
    if postre not in POSTRES:
        POSTRES[postre] = ingredientes
        print(f"Postre {postre} agregado con ingredientes: {POSTRES[postre]}")
    else:
        print(f"El postre {postre} ya existe")

def baja_postre(postre):
    if postre in POSTRES:
        del POSTRES[postre]
        print(f"Postre {postre} eliminado")
    else:
        print(f"No se encontró el postre {postre}")

def eliminar_repetidos():
    for postre, ingredientes in POSTRES.items():
        POSTRES[postre] = list(set(ingredientes))
    print("Se han eliminado los elementos repetidos de las listas de ingredientes")

def ingresar_ingredientes():
    ingredientes = []
    while True:
        ingrediente = input("Ingrese un ingrediente (o escriba 'fin' para terminar): ")
        if ingrediente.lower() == 'fin':
            break
        ingredientes.append(ingrediente)
    return ingredientes

while True:
    print("\nMenú:")
    print("1. Imprimir ingredientes de un postre")
    print("2. Insertar ingredientes a un postre")
    print("3. Eliminar ingredientes de un postre")
    print("4. Dar de alta un postre")
    print("5. Dar de baja un postre")
    print("6. Eliminar repetidos de las listas de ingredientes")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        postre = input("Ingrese el nombre del postre: ")
        imprimir_ingredientes(postre)
    elif opcion == '2':
        postre = input("Ingrese el nombre del postre: ")
        ingredientes = ingresar_ingredientes()
        insertar_ingredientes(postre, ingredientes)
    elif opcion == '3':
        postre = input("Ingrese el nombre del postre: ")
        ingredientes = ingresar_ingredientes()
        eliminar_ingredientes(postre, ingredientes)
    elif opcion == '4':
        postre = input("Ingrese el nombre del postre: ")
        ingredientes = ingresar_ingredientes()
        alta_postre(postre, ingredientes)
    elif opcion == '5':
        postre = input("Ingrese el nombre del postre: ")
        baja_postre(postre)
    elif opcion == '6':
        eliminar_repetidos()
    elif opcion == '7':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
