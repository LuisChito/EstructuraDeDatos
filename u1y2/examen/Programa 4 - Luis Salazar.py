import random

def llenar_vector_aleatorio(n):
    vector = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(random.randint(1, 100))
        vector.append(fila)
    return vector

def sumar_vectores(vector_a, vector_b):
    n = len(vector_a)
    resultado = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(vector_a[i][j] + vector_b[i][j])
        resultado.append(fila)
    return resultado

def restar_vectores(vector_a, vector_b):
    n = len(vector_a)
    resultado = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(vector_b[i][j] - vector_a[i][j])
        resultado.append(fila)
    return resultado

def imprimir_vector(vector):
    for fila in vector:
        print(fila)

def main():
    print("Bienvenido al programa")
    n = int(input("Ingrese la cantidad de celdas para los vectores (n x n): "))
    
    while True:
        opcion = int(input("\nElija una opción:\n1. Llenar vector A de manera aleatoria.\n2. Llenar vector B de manera aleatoria.\n3. Sumar vector A y vector B.\n4. Restar vector B menos vector A.\n5. Salir\n"))

        if opcion == 1:
            vector_a = llenar_vector_aleatorio(n)

        elif opcion == 2:
            vector_b = llenar_vector_aleatorio(n)
            
        elif opcion == 3:
            vector_c = sumar_vectores(vector_a, vector_b)
            
        elif opcion == 4:
            vector_d = restar_vectores(vector_a, vector_b)
            
        elif opcion == 5:
            opcionVector = input("Elije el vector que deseas imprimir (A, B, C, D): ")
            if opcionVector == "A":
                print("\nEl vector A llenado de manera aleatoria es:")
                imprimir_vector(vector_a)

            elif opcionVector == "B":
                print("\nEl vector B llenado de manera aleatoria es:")
                imprimir_vector(vector_b)

            elif opcionVector == "C":
                print("\nEl vector C, resultado de la suma de A y B, es:")
                imprimir_vector(vector_c)

            elif opcionVector == "D":
                print("\nEl vector D, resultado de la resta de B y A, es:")
                imprimir_vector(vector_d)

        elif opcion == 6:
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida")

if __name__ == "__main__":
    main()
