calificaciones = [0, 0, 0, 0, 0]

for i in range(5):
    calificacion = float(input(f"Ingrese la calificación {i+1}: "))
    calificaciones[i] = calificacion

print("Las calificaciones son:")
print(calificaciones)