import sys
import ejercicio1, ejercicio2, ejercicio3, ejercicio4, ejercicio5

def mostrar_menu():
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Intercalar archivos y formar RECITALES")
    print("5. Salir")

def ejecutar_opcion(opcion):
    if opcion == '1':
        print("Hoteles")
        ejercicio1.main()

    elif opcion == '2':
        print("Datos Alumnos")
        ejercicio2.main()

    elif opcion == '3':
        print("Empleados")
        ejercicio3.main()
        
    elif opcion == '4':
        print("Recitales")
        ejercicio4.main()

    elif opcion == '5':
        print("Alumnos Promedios")
        ejercicio5.main()
    
    elif opcion == '6':
        print("Saliendo del programa...")
        sys.exit()
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        ejecutar_opcion(opcion)
