import matplotlib.pyplot as plt

def bellman_ford(n, edges, source):
    dist = [float('inf')] * n
    dist[source] = 0

    # главный цикл расслабления
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
    # параметры графа
    n = 4
    edges = [
        (0, 1, 5),
        (1, 2, 3),
        (2, 3, 1),
        (1, 3, 1),
        (0, 2, -2),
        (0, 3, 10)
    ]
    source = 0

    distances = bellman_ford(n, edges, source)
    print(f"Distances from {source}: {distances}")

    # фиксированные координаты для визуализации
    pos = {
        0: (0, 0),
        1: (1, 1),
        2: (2, 0),
        3: (3, 1)
    }

    fig, ax = plt.subplots()

    # рисуем вершины и их расстояния
    for node, (x, y) in pos.items():
        ax.scatter(x, y, s=500, color='skyblue', zorder=2)
        ax.text(x, y + 0.12, str(node),
                ha='center', va='bottom', zorder=3, fontsize=12)
        ax.text(x, y - 0.12, str(distances[node]),
                ha='center', va='top', color='red', zorder=3, fontsize=12)

    # рисуем ребра, стрелки и подписи весов
    for u, v, w in edges:
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        dx, dy = x2 - x1, y2 - y1

        # стрелка
        ax.arrow(
            x1, y1,
            dx * 0.8, dy * 0.8,
            head_width=0.1,
            length_includes_head=True,
            color='gray',
            zorder=1
        )

        # вычисляем маленький смещённый вектор перпендикуляра
        perp_x, perp_y = -dy, dx
        norm = (perp_x**2 + perp_y**2)**0.5 or 1
        perp_x = perp_x / norm * 0.1
        perp_y = perp_y / norm * 0.1

        # подпись веса
        ax.text(
            x1 + dx * 0.5 + perp_x,
            y1 + dy * 0.5 + perp_y,
            str(w),
            ha='center', va='center',
            backgroundcolor='white',
            zorder=4,
            fontsize=10
        )

    ax.set_title('Граф и кратчайшие расстояния (Bellman–Ford)')
    ax.axis('off')
    ax.margins(0.1)
    plt.tight_layout()
    plt.show()
