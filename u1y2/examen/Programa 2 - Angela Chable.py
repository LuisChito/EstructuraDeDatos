class ArreglosUnidimensionales:
    def __init__(self):
        TamañoArreglos = int(input("Introducir el tamaño de los arreglos unidimensionales: "))
        self.nombres = []
        self.longitudes = []

        for i in range(TamañoArreglos):
            NombrePersonal = input(f"Ingrese el nombre de la persona {i+1}: ")
            self.nombres.append(NombrePersonal)
            self.longitudes.append(len(NombrePersonal))

    def mostrar_datos(self):
        print("\nLos Nombres y las longitudes son:")
        for NombrePersonal, Longitud in zip(self.nombres, self.longitudes):
            print(f"Nombre: {NombrePersonal}, Longitud: {Longitud}")

def main():
    arreglo = ArreglosUnidimensionales()
    arreglo.mostrar_datos()

main()
