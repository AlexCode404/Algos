import random
import time
import matplotlib.pyplot as plt
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
    algorithm(data.copy())
    return time.perf_counter() - start


import json

# Конфигурация тестирования
with open('config.json', 'r') as f:
    config = json.load(f)
    
algorithms = config['algorithms']
sizes = config['array_sizes']
data_types = config['data_types']

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

# Сбор результатов времени выполнения для каждого алгоритма и типа данных
results = {algo_name: {dtype: [] for dtype in data_types} for algo_name in algorithms}

print("Начало тестирования алгоритмов сортировки строк...")
for size in sizes:
    for dtype_name, dtype in data_types.items():
        test_data = generate_data(size, dtype)
        for algo_name, algorithm in algorithms.items():
            time_taken = test_algorithm(algorithm, test_data)
            results[algo_name][dtype_name].append(time_taken)
            print(f'{algo_name} | {dtype_name} | {size} элементов: {time_taken:.5f} сек')

# Построение графиков производительности для каждого алгоритма
for algo_name in algorithms:
    plt.figure(figsize=(10, 6))
    for dtype_name in data_types:
        plt.plot(
            sizes,
            results[algo_name][dtype_name],
            marker='o',
            label=f'{dtype_name.capitalize()} case'
        )
    plt.title(f'{algo_name}')
    plt.xlabel('Размер массива')
    plt.ylabel('Время (секунды)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.savefig(f'{algo_name.lower().replace(" ", "_")}_GRAPH.png', dpi=300, bbox_inches='tight')
    plt.close()

print("Графики сохранены в PNG-файлы.")