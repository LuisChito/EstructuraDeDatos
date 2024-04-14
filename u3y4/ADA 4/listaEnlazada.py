class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None  

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self):
        while True:
            try:
                dato = int(input("Ingrese un numero entero para agregar a la lista: "))
                nuevo_nodo = Nodo(dato)
                if self.cabeza is None:
                    self.cabeza = nuevo_nodo
                else:
                    actual = self.cabeza
                    while actual.siguiente:
                        actual = actual.siguiente
                    actual.siguiente = nuevo_nodo
                break
            except ValueError:
                print("Solo se aceptan numeors enteros >:)")

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.datos, end=" -> ")
            actual = actual.siguiente
        print("None")

mi_lista = ListaEnlazada()
mi_lista.agregar()
mi_lista.agregar()
mi_lista.agregar()
mi_lista.imprimir()

