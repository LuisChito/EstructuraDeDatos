def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print (arr)
        for j in range(0, n-i-1):
            print(arr)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [45, 17, 23, 67, 21]
bubble_sort(arr)
print("Lista ordenada usando Burbuja:")
print(arr)
