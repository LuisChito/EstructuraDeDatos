def Terreno_inical():
    return float(input("Ingrese la superficie inicial del terreno: "))

def Generaciones():
    return int(input("Ingrese el número de generaciones: "))

def Herederos():
    return int(input("Ingrese el número de herederos por generación: "))

def TerrenoXGeneracion(S_I, generacion, HXG):
    herederos_actuales = HXG ** generacion
    superficie_actual = S_I / herederos_actuales
    return superficie_actual

def main():
    S_I = Terreno_inical()
    generaciones = Generaciones()
    HXG = Herederos()

    if generaciones > 50:
        print("El número máximo de generaciones es 50")
        return

    print("\nCantidad de terreno por generación:")
    for generacion in range(generaciones):
        superficie_generacion = TerrenoXGeneracion(S_I, generacion, HXG)
        print(f"Generación {generacion}: {superficie_generacion:.2f} metros cuadrados")

if __name__ == "__main__":
    main()
