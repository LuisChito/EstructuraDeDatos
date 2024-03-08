class ArreglosUnidimensionales:
    def _init_(self):
        while True:
            tamaño_input = input("Introducir el tamaño de los arreglos unidimensionales: ")
            if tamaño_input.isdigit():
                self.tamaño_arreglos = int(tamaño_input)
                break
            else:
                print("Error: Por favor, ingrese un tamaño válido (número entero).")

        self.nombres = []
        self.longitudes = []

        for i in range(self.tamaño_arreglos):
            while True:
                nombre_personal = input(f"Ingrese el nombre de la persona {i+1}: ")
                if nombre_personal.isalpha():
                    self.nombres.append(nombre_personal)
                    self.longitudes.append(len(nombre_personal))
                    break
                else:
                    print("Error: Por favor, ingrese un nombre válido sin números ni caracteres especiales.")

    def mostrar_datos(self):
        print("\nLos Nombres y las longitudes son:")
        for nombre_personal, longitud in zip(self.nombres, self.longitudes):
            print(f"Nombre: {nombre_personal}, Longitud: {longitud}")

def main():
    arreglo = ArreglosUnidimensionales()
    arreglo.mostrar_datos()

main()