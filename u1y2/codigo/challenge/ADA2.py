num_alumnos = 100
num_materias = 5

calificaciones = [[0] * num_materias for _ in range(num_alumnos)]

for i in range(num_alumnos):
    print(f"Ingrese las calificaciones del alumno {i+1}:")
    for j in range(num_materias):
        calificacion = float(input(f"Calificación en materia {j+1}: "))
        calificaciones[i][j] = calificacion

print("\nCalificaciones ingresadas:")

alumno_95_index = 94 
print(f"Calificaciones del alumno {alumno_95_index + 1}: {calificaciones[alumno_95_index]}")
