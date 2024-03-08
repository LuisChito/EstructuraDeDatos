def Terreno_inicial():
    return float(input("Ingrese la superficie inicial del terreno: "))

def Generaciones():
    while True:
        num_generaciones = int(input("Ingrese el número de generaciones: "))
        if num_generaciones <= 50:
            return num_generaciones
        else:
            print("Error: El número máximo de generaciones es 50. Por favor, ingrese un valor menor o igual a 50.")

def Herederos():
    return int(input("Ingrese el número de herederos por generación: "))

def TerrenoXGeneracion(S_I, generacion, HXG):
    herederos_actuales = HXG ** generacion
    superficie_actual = S_I / herederos_actuales
    return superficie_actual

def main():
    S_I = Terreno_inicial()
    generaciones = Generaciones()
    HXG = Herederos()

    print("\nCantidad de terreno por generación:")
    for generacion in range(generaciones):
        superficie_generacion = TerrenoXGeneracion(S_I, generacion, HXG)
        print(f"Generación {generacion}: {superficie_generacion:.2f} metros cuadrados")

if __name__ == "__main__":
    main()
