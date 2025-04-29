import matplotlib.pyplot as plt

# Bellman–Ford: кратчайшие пути во взвешенном графе

def bellman_ford(n, edges, source):
    """
    n       – число вершин (0..n-1)
    edges   – список троек (u, v, w)
    source  – стартовая вершина
    возвращает список dist, где dist[v] = длина кратчайшего пути из source в v
    выбрасывает ValueError, если найден отрицательный цикл
    """
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


if __name__ == "__main__":
    # Настройка графа
    n = 4
    edges = [
        (0, 1, 5),    # из вершины 0 в 1 вес 5
        (1, 2, 3),    # из вершины 1 в 2 вес 3
        (2, 3, 1),    # из вершины 2 в 3 вес 1
        (1, 3, 1),    # из вершины 1 в 3 вес 1
        (0, 2, -2),   # отрицательное ребро из 0 в 2 вес -2
        (0, 3, 10)    # из вершины 0 в 3 вес 10
    ]
    source = 0

    # Вычисление кратчайших путей
    distances = bellman_ford(n, edges, source)
    print("Distances from {}: {}".format(source, distances))  # [0, 5, -2, -1]

    # Простейшая визуализация графа и расстояний
    # задаём фиксированные координаты для вершин
    pos = {
        0: (0, 0),
        1: (1, 1),
        2: (2, 0),
        3: (3, 1)
    }

    fig, ax = plt.subplots()
    # рисуем вершины
    for node, (x, y) in pos.items():
        ax.scatter(x, y, s=500, color='skyblue', zorder=2)
        # отдельно рисуем номер вершины и расстояние разными цветами
        ax.text(x, y + 0.1, str(node), ha='center', va='bottom', zorder=3, color='black', fontsize=12)
        ax.text(x, y - 0.1, str(distances[node]), ha='center', va='top', zorder=3, color='red', fontsize=12)

    # рисуем ребра со стрелками и подписями весов
    for u, v, w in edges:
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        dx, dy = x2 - x1, y2 - y1
        ax.arrow(x1, y1, dx * 0.8, dy * 0.8,
                 head_width=0.1, length_includes_head=True, color='gray', zorder=1)
        # подпись веса посередине ребра
        ax.text(x1 + dx * 0.5, y1 + dy * 0.5, str(w), ha='center', va='center', backgroundcolor='white')

    ax.set_title('Граф и кратчайшие расстояния (Bellman–Ford)')
    ax.axis('off')
    plt.tight_layout()
    plt.show()
