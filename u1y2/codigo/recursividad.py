def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
 
while True:
    numero = int(input("Ingrese un número para calcular su factorial (o ingrese '0' para salir): "))
    if numero == 0:
        print("¡Hasta luego!")
        break
    else:
        print("El factorial de", numero, "es", factorial(numero))
