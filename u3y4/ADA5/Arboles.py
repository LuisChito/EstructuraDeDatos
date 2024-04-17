class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._agregar_recursivo(self.raiz, dato)

    def _agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._agregar_recursivo(nodo.derecha, dato)

    def imprimir_inorden(self):
        self._imprimir_inorden_recursivo(self.raiz)
        print()

    def _imprimir_inorden_recursivo(self, nodo):
        if nodo:
            self._imprimir_inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=' ')
            self._imprimir_inorden_recursivo(nodo.derecha)

if __name__ == "__main__":
    arbol = Arbol()
    while True:
        obj = int(input(f"Ingrese un numero para agregar al arbol, o ingrese '0' para salir e imprimir el orden: "))
        if obj == 0:
            print("Orden del arbol:")
            arbol.imprimir_inorden()
            break
        else:
            arbol.agregar(obj)
            

    

