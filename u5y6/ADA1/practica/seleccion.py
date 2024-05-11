def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        print(arr)
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [26, 54, 93, 17, 77, 55, 31, 20, 40]
selection_sort(arr)
print("Lista ordenada usando Por Selección:")
print(arr)
