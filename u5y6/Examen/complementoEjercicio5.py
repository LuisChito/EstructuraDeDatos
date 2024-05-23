def agregar_alumno(alumnos):
    nombre = input("Ingrese el nombre del alumno: ").strip().upper()
    materias = ['Estructuras de Datos', 'Sistemas Operativos', 'Calculo Vectorial', 'Contabilidad Financiera', 'Física General', 'Investigacion de Operaciones']
    calificaciones = {}
    aprobadas = []

    for materia in materias:
        calificacion = float(input(f"Ingrese la calificación de {materia}: "))
        calificaciones[materia] = calificacion
        if calificacion >= 70:
            aprobadas.append(materia)

    alumnos.append({'nombre': nombre, 'calificaciones': calificaciones, 'aprobadas': aprobadas})
    print("Alumno agregado exitosamente.\n")


def mostrar_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos registrados.\n")
        return

    print("{:<20} {:<10} {:<40}".format("Nombre", "Promedio", "Materias Aprobadas"))
    print("-" * 75)

    for alumno in alumnos:
        nombre = alumno['nombre']
        promedio = calcular_promedio(alumnos, nombre)
        materias_aprobadas = ', '.join(alumno['aprobadas'])

        print("{:<20} {:<10.2f} {:<40}".format(nombre, promedio, materias_aprobadas))

def buscar_reprobadas(alumnos, nombre):
    for alumno in alumnos:
        if alumno['nombre'] == nombre:
            reprobadas = [materia for materia, calificacion in alumno['calificaciones'].items() if calificacion < 60]
            return reprobadas
    return None


def consultar_alumno(alumnos, nombre_completo):
    nombre_completo = nombre_completo.strip().upper()  # Convertir a mayúsculas

    encontrado = False
    for alumno in alumnos:
        nombre_apellido = alumno['nombre'].upper()
        if nombre_apellido == nombre_completo:
            promedio = calcular_promedio(alumnos, alumno['nombre'])
            print(f"Nombre: {alumno['nombre']}")
            print(f"Promedio: {promedio:.2f}")
            print("Calificaciones:")
            for materia, calificacion in alumno['calificaciones'].items():
                print(f"  {materia}: {calificacion}")
            print("Materias Aprobadas:", ", ".join(alumno['aprobadas']))
            encontrado = True
            break

    if not encontrado:
        print(f"Estudiante {nombre_completo} no encontrado.\n")

def listar_nombres(alumnos):
    if not alumnos:
        print("No hay alumnos registrados.\n")
        return
    print("Lista de alumnos registrados:")
    for alumno in alumnos:
        print(f" - {alumno['nombre']}")
    print()

def calcular_promedio(alumnos, nombre):
    for alumno in alumnos:
        if alumno['nombre'] == nombre:
            calificaciones = alumno['calificaciones'].values()
            if calificaciones:
                promedio = sum(calificaciones) / len(calificaciones)
                return promedio
    return None