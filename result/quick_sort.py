import time
import random
import sys

sys.setrecursionlimit(100000) 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    elem = arr[0]
    left = [x for x in arr if x < elem]
    center = [x for x in arr if x == elem]
    right = [x for x in arr if x > elem]

    return quick_sort(left) + center + quick_sort(right)

test = [
    5,102,4,105,651,301
]

start_time = time.time()
print("\nСортировка большого списка строк:")
print(quick_sort(test))
end_time = time.time()
print(f"Время выполнения: {end_time - start_time:.6f} секунд")