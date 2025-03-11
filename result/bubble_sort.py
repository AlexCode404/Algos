def bubble_sort(arr):
    n = len(arr)  
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j + 1]:           
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


for i in range(2):
    print(i)