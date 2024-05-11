def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(arr)

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(arr)
print("Lista ordenada usando Por Inserción:")
print(arr)
