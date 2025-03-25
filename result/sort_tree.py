import time


def sort_tree(arr):
    if not arr:
        return []
    
    elem, *rest = arr  
    left = [x for x in rest if x < elem]  
    right = [x for x in rest if x >= elem]  
    
    print([elem])
    return sort_tree(left) + [elem] + sort_tree(right)  


test = [
    5,102,4,105,651,301
]

start_time = time.time()
print("\nСортировка большого списка строк:")
print(sort_tree(test))
end_time = time.time()
print(f"Время выполнения: {end_time - start_time:.6f} секунд")
