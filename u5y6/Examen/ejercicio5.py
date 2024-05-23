from complementoEjercicio5 import agregar_alumno, mostrar_alumnos, buscar_reprobadas, consultar_alumno, calcular_promedio

def main():
    alumnos = [
        {
            'nombre': 'ALEJANDRO QUIJANO',
            'promedio': 75.0,
            'calificaciones': {
                'Estructuras de Datos': 80,
                'Sistemas Operativos': 70,
                'Calculo Vectorial': 65,
                'Contabilidad Financiera': 78,
                'Física General': 82,
                'Investigacion de Operaciones': 70
            },
            'aprobadas': ['Estructuras de Datos', 'Sistemas Operativos', 'Calculo Vectorial', 'Contabilidad Financiera',
                          'Física General', 'Investigacion de Operaciones']
        },
        {
            'nombre': 'ANA GOMEZ',
            'promedio': 68.5,
            'calificaciones': {
                'Estructuras de Datos': 60,
                'Sistemas Operativos': 55,
                'Calculo Vectorial': 72,
                'Contabilidad Financiera': 70,
                'Física General': 69,
                'Investigacion de Operaciones': 85
            },
            'aprobadas': ['Estructuras de Datos', 'Calculo Vectorial', 'Contabilidad Financiera',
                          'Investigacion de Operaciones']
        },
        {
            'nombre': 'LUIS RODRIGUEZ',
            'promedio': 83.0,
            'calificaciones': {
                'Estructuras de Datos': 90,
                'Sistemas Operativos': 85,
                'Calculo Vectorial': 88,
                'Contabilidad Financiera': 80,
                'Física General': 75,
                'Investigacion de Operaciones': 80
            },
            'aprobadas': ['Estructuras de Datos', 'Sistemas Operativos', 'Calculo Vectorial', 'Contabilidad Financiera',
                          'Física General', 'Investigacion de Operaciones']
        }
    ]
    
    while True:
        print("Menú:")
        print("1. Consultar información de un alumno")
        print("2. Mostrar todos los alumnos")
        print("3. Buscar materias reprobadas por un alumno")
        print("4. Calcular promedio final de un alumno")
        print("5. Agregar alumno")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            consultar_alumno(alumnos, nombre_alumno)
        elif opcion == '2':
            mostrar_alumnos(alumnos)
        elif opcion == '3':
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            reprobadas = buscar_reprobadas(alumnos, nombre_alumno)
            if reprobadas is not None:
                if reprobadas:
                    print(f"{nombre_alumno} ha reprobado las siguientes materias: {', '.join(reprobadas)}\n")
                else:
                    print(f"{nombre_alumno} no ha reprobado ninguna materia.\n")
            else:
                print(f"Estudiante {nombre_alumno} no encontrado.\n")
        elif opcion == '4':
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            promedio = calcular_promedio(alumnos, nombre_alumno)
            if promedio is not None:
                print(f"El promedio final de {nombre_alumno} es {promedio}\n")
            else:
                print(f"Estudiante {nombre_alumno} no encontrado.\n")
        elif opcion == '5':
            agregar_alumno(alumnos)
        elif opcion == '6':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()
