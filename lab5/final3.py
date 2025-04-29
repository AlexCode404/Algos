
# Задача 2. Bellman–Ford: кратчайшие пути во взвешенном графе (возможно отрицательные веса, без отрицательных циклов).

def bellman_ford(n, edges, source):
    dist = [float('inf')] * n
    dist[source] = 0

    # расслабляем рёбра n-1 раз
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    # проверка на отрицательные циклы
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Граф содержит цикл с отрицательным весом.")

    return dist


# Пример использования:
if __name__ == "__main__":
    n = 4
    edges = [
        (0, 1, 5),    # из вершины 0 в 1 вес 5
        (1, 2, 3),    # из вершины 1 в 2 вес 3
        (2, 3, 1),    # из вершины 2 в 3 вес 1
        (1, 3, 1),    # из вершины 1 в 3 вес 1
        (0, 2, -2),   # добавлено отрицательное ребро из 0 в 2 вес -2
        (0, 3, 10),    # из вершины 0 в 3 вес 
        
    ]
    print("Distances:", bellman_ford(n, edges, 0))
