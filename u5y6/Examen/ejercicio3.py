class Empleado:
    def __init__(self, nombre, estado_civil, antiguedad, categoria, sueldo):
        self.nombre = nombre
        self.estado_civil = estado_civil
        self.antiguedad = antiguedad
        self.categoria = categoria
        self.sueldo = sueldo

    def __repr__(self):
        return f"{self.nombre},{self.estado_civil},{self.antiguedad},{self.categoria},{self.sueldo}"

def leer_empleados():
    empleados = [
        Empleado("JuanPérez", "Soltero", 5, "A", 3000.50),
        Empleado("AnaGómez", "Casada", 10, "B", 4000.75),
        Empleado("CarlosSánchez", "Soltero", 3, "A", 2500.00),
        Empleado("MaríaRodríguez", "Casada", 8, "C", 3500.80),
        Empleado("PedroMartínez", "Viudo", 15, "D", 5000.90),
        Empleado("Julieta", "Soltera", 1, "A", 3000.50),
        Empleado("Ramona", "Casada", 10, "B", 4000.75),
        Empleado("Naomi", "Soltero", 58, "A", 2500.00),
        Empleado("Juana", "Casada", 30, "C", 3500.80),
        Empleado("Pancrasia", "Viudo", 40, "D", 5000.90),
        Empleado("Luis", "Soltero", 2, "A", 3000.50),
        Empleado("Esmeralda", "Casada", 5, "B", 4000.75),
        Empleado("Romea", "Soltero", 12, "A", 2500.00),
        Empleado("Tanos", "Casada", 89, "C", 3500.80),
        Empleado("PedritoSola", "Viudo", 16, "D", 5000.90),
        Empleado("PerezJuan", "Soltero", 50, "A", 3000.50),
        Empleado("Airam", "Casada", 94, "B", 4000.75),
        Empleado("Esau", "Soltero", 28, "A", 2500.00),
        Empleado("Fercho", "Casada", 25, "C", 3500.80),
        Empleado("Claudia", "Viudo", 38, "D", 5000.90),
        Empleado("Ibrahim", "Soltero", 14, "A", 3000.50),
        Empleado("Diego", "Casada", 100, "B", 4000.75),
        Empleado("Alex", "Soltero", 50, "A", 2500.00),
        Empleado("Juancho", "Casada", 2, "C", 3500.80),
        Empleado("Irma", "Viudo", 40, "D", 5000.90)
    ]
    return empleados

def imprimir_empleados(empleados):
    for empleado in empleados:
        print(f"{empleado}")

def mezcla_directa(empleados):
    if len(empleados) > 1:
        mid = len(empleados) // 2
        left_half = empleados[:mid]
        right_half = empleados[mid:]

        mezcla_directa(left_half)
        mezcla_directa(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].nombre < right_half[j].nombre:
                empleados[k] = left_half[i]
                i += 1
            else:
                empleados[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            empleados[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            empleados[k] = right_half[j]
            j += 1
            k += 1

def mezcla_equilibrada(empleados):
    def dividir_archivo(empleados):
        n = len(empleados)
        f1 = []
        f2 = []
        for i in range(n):
            if i % 2 == 0:
                f1.append(empleados[i])
            else:
                f2.append(empleados[i])
        return f1, f2

    def mezclar_archivos(f1, f2):
        resultado = []
        i = j = 0
        while i < len(f1) and j < len(f2):
            if f1[i].nombre < f2[j].nombre:
                resultado.append(f1[i])
                i += 1
            else:
                resultado.append(f2[j])
                j += 1

        while i < len(f1):
            resultado.append(f1[i])
            i += 1

        while j < len(f2):
            resultado.append(f2[j])
            j += 1

        return resultado

    f1, f2 = dividir_archivo(empleados)
    empleados_ordenados = mezclar_archivos(f1, f2)
    return empleados_ordenados

def main():
    empleados = leer_empleados()

    print("Empleados ordenados por mezcla directa:")
    mezcla_directa(empleados)
    imprimir_empleados(empleados)

    empleados = leer_empleados()

    print("\nEmpleados ordenados por mezcla equilibrada:")
    empleados_ordenados_equilibrada = mezcla_equilibrada(empleados)
    imprimir_empleados(empleados_ordenados_equilibrada)

if __name__ == "__main__":
    main()
