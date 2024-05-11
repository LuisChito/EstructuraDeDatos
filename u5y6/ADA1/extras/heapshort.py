import matplotlib.pyplot as plt
import numpy as np

# Generar datos para n y su correspondiente valor O(n log n)
n = np.linspace(1, 10, 100)  # Rango de valores de n
o_n_log_n = n * np.log(n)

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot(n, o_n_log_n, label='O(n log n)', color='blue')

# Añadir etiquetas y título
plt.title('Gráfica de la función O(n log n)')
plt.xlabel('n')
plt.ylabel('O(n log n)')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()
