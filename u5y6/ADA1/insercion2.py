def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i
        
        # Desplaza los elementos de la lista que son mayores que el valor actual
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        
        # Inserta el valor actual en su posición correcta
        arr[position] = current_value

# Ejemplo de uso:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Lista ordenada usando Por Inserción:")
print(arr)
