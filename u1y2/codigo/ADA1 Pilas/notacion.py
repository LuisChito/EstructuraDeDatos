class Pila:
    def __init__(self):
        self.elementos = []

    def vacio(self):
        return self.elementos == []

    def apilar(self, item):
        self.elementos.append(item)

    def desapilar(self):
        return self.elementos.pop()


def posfijo(expresion):
    pila = Pila()
    operandos = expresion.split()

    for token in operandos:
        if token.isdigit():
            pila.apilar(int(token))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            resultado = realizar(token, operando1, operando2)
            pila.apilar(resultado)

    return pila.desapilar()


def prefijo(expresion):
    pila = Pila()
    operandos = expresion.split()

    operandos.reverse()
    for token in operandos:
        if token.isdigit():
            pila.apilar(int(token))
        else:
            operando1 = pila.desapilar()
            operando2 = pila.desapilar()
            resultado = realizar(token, operando1, operando2)
            pila.apilar(resultado)

    return pila.desapilar()


def realizar(operador, op1, op2):
    if operador == '+':
        return op1 + op2
    elif operador == '-':
        return op1 - op2
    elif operador == '*':
        return op1 * op2
    elif operador == '/':
        return op1 / op2
    else:
        raise ValueError("Operador no válido")


expresion = input("Ingrese la expresión a evaluar: ")
tipo_notacion = input("Ingrese 'posfija' o 'prefija' para seleccionar la notación: ")

if tipo_notacion == "posfija":
    resultado = posfijo(expresion)
    print("El resultado de la expresión posfija es:", resultado)
elif tipo_notacion == "prefija":
    resultado = prefijo(expresion)
    print("El resultado de la expresión prefija es:", resultado)
else:
    print("Notación no válida. Por favor, ingrese 'posfija' o 'prefija'.")
