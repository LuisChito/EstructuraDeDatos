def es_numerico(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


def alumnos():
    while True:
        alumestruc = input("Ingresa los IDs de los alumnos que estudian Estructura (separalos con un espacio) :").split()
        alumprogra = input("Ingresa los IDs de los alumnos que estudian Programación (separalos con un espacio) :").split()

        if all(es_numerico(alumno) for alumno in alumestruc + alumprogra):
            break
        else:
            print("Error: Se ingresó un valor no numérico. Por favor, intenta de nuevo.")

    estruc = alumestruc
    progra = alumprogra

    comunes = [alumno for alumno in estruc if alumno in progra]
    comunes = list(set(comunes))
    cantidad = len(comunes)

    print("Los IDs de los alumnos comunes en ambas asignaturas son: ")
    for alumno in comunes:
        print(alumno)

    print(f"La cantidad de alumnos comunes son: {cantidad}")


alumnos()
