class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        destino.apilar(origen.desapilar())
        print("Mover disco de {} a {}".format(origen, destino))
    else:
        hanoi(n - 1, origen, auxiliar, destino)
        hanoi(1, origen, destino, auxiliar)
        hanoi(n - 1, auxiliar, destino, origen)


torre_A = Pila()
torre_B = Pila()
torre_C = Pila()


for disco in range(3, 0, -1):
    torre_A.apilar(disco)


print("Estado inicial:")
print("Torre A:", torre_A.items)
print("Torre B:", torre_B.items)
print("Torre C:", torre_C.items)
hanoi(3, torre_A, torre_C, torre_B)
print("\nEstado final:")
print("Torre A:", torre_A.items)
print("Torre B:", torre_B.items)
print("Torre C:", torre_C.items)
