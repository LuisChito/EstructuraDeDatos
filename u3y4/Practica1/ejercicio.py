class Pila:
    def __init__(self, capMaxima):
        self.items = []
        self.capMaxima = capMaxima
        self.tope = 0

    def vacia(self):
        return self.tope == 0

    def llena(self):
        return self.tope == self.capMaxima

    def poner(self, elemento):
        if self.llena():
            print("Error: la pila está llena")
            return
        self.items.append(elemento)
        self.tope += 1
        self.actual()

    def eliminar(self):
        if self.vacia():
            print("Pila está vacía")
            return
        elemento_eliminado = self.items.pop()
        self.tope -= 1
        print(f"Elemento eliminado: {elemento_eliminado}")
        self.actual()

    def actual(self):   
        print(f"Pila: {self.items}, TOPE = {self.tope}")


pila = Pila(capMaxima=8)

while True:
    print("Qué quieres hacer?")
    opcion = input("Eliminar, agregar o salir?: ")
    if opcion == "agregar":
        n = input("Agregar: ")
        pila.poner(n)
    elif opcion == "eliminar":
        pila.eliminar()
    else:
        break

