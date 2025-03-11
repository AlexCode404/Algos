import random
import time
import json
import numpy as np

# Импорт алгоритмов сортировки
from bubble_sort import bubble_sort
from insert_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heapsort
from sort_tree import sort_tree
from red_black_sort import create_tree_with_data
from radix_sort import radix_sort


def generate_data(n, data_type='random'):
    """Генерация данных разных типов для тестирования"""
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_strings = [''.join(random.choices(chars, k=random.randint(3, 10))) for _ in range(n)]
    
    if data_type == 'sorted':
        return sorted(random_strings)
    elif data_type == 'reverse_sorted':
        return sorted(random_strings, reverse=True)
    return random_strings


def test_algorithm(algorithm, data):
    """Тестирование алгоритма с замером времени"""
    start = time.perf_counter()
    algorithm(data.copy())  # Используем копию данных, чтобы не изменять оригинал
    return time.perf_counter() - start


# Загрузка конфигурации из JSON
with open('config.json', 'r') as f:
    config = json.load(f)

algorithms = {
    'Bubble Sort': bubble_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort,
    'Radix Sort': radix_sort,
    'Heap Sort': heapsort,
    "Red Black Sort": create_tree_with_data,
    'Tree Sort': sort_tree
}

sizes = config['array_sizes']
data_types = config['data_types']

# Теоретическая сложность алгоритмов
complexities = {
    'Bubble Sort': lambda n: n**2,
    'Insertion Sort': lambda n: n**2,
    'Merge Sort': lambda n: n * np.log2(n),
    'Quick Sort': lambda n: n * np.log2(n),
    'Radix Sort': lambda n: n,  # В среднем O(n)
    'Heap Sort': lambda n: n * np.log2(n),
    "Red Black Sort": lambda n: n * np.log2(n),
    'Tree Sort': lambda n: n * np.log2(n),
}

# Хранение результатов времени выполнения
results = {algo: {dtype: [] for dtype in data_types} for algo in algorithms}
coefficients = {algo: {dtype: 0 for dtype in data_types} for algo in algorithms}

print("Начало тестирования алгоритмов сортировки строк...")

# Запуск тестирования
for size in sizes:
    for dtype_name, dtype in data_types.items():
        test_data = generate_data(size, dtype)
        for algo_name, algorithm in algorithms.items():
            time_taken = test_algorithm(algorithm, test_data)
            results[algo_name][dtype_name].append(time_taken)
            print(f'{algo_name} | {dtype_name} | {size} элементов: {time_taken:.5f} сек')

# Вычисление коэффициента C
for algo_name in algorithms:
    for dtype_name in data_types:
        C_values = []
        for i, size in enumerate(sizes):
            if size == 0:
                continue  # Пропускаем нулевой размер
            f_n = complexities[algo_name](size)
            if f_n > 0:
                C = results[algo_name][dtype_name][i] / f_n
                C_values.append(C)
        
        if C_values:
            coefficients[algo_name][dtype_name] = np.mean(C_values)  # Усреднение коэффициента

# Вывод коэффициентов C
print("\nКоэффициенты C для каждого алгоритма:")
for algo_name in algorithms:
    print(f'\n{algo_name}:')
    for dtype_name, C in coefficients[algo_name].items():
        print(f'  {dtype_name}: {C:.8f}')
