def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1  

    while max_val // exp > 0:
        n = len(arr)
        output = [0] * n       
        count = [0] * 10       

        for number in arr:
            index = (number // exp) % 10
            count[index] += 1

        
        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        arr = output[:]
        exp *= 10

    return arr

arr = [307, 50, 10, 5]
sorted_arr = radix_sort(arr)
print("Отсортированный массив:", sorted_arr)

