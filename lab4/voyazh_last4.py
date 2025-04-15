def calculate_cost(path, matrix):
    cost = 0
    for i in range(len(path) - 1):
        cost += matrix[path[i]][path[i + 1]]
    return cost


def perm(lst, n, matrix, best):
    if n < 2:
        path = [0] + lst + [0]  # маршрут с возвратом
        cost = calculate_cost(path, matrix)
        if cost < best['cost']:
            best['cost'] = cost
            best['path'] = path[:]
    else:
        for j in range(n - 1, -1, -1):
            lst[j], lst[n - 1] = lst[n - 1], lst[j]
            perm(lst, n - 1, matrix, best)
            lst[j], lst[n - 1] = lst[n - 1], lst[j]


def solve_tsp(matrix):
    n = len(matrix)
    cities = list(range(1, n))  # без стартового города

    best = {'cost': float('inf'), 'path': []}
    perm(cities, len(cities), matrix, best)

    return best['path'], best['cost']


# Пример: матрица расстояний
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Запуск
best_path, best_cost = solve_tsp(distance_matrix)
print("Лучший маршрут:", best_path)
print("Минимальная стоимость:", best_cost)
