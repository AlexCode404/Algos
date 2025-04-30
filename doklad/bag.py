def grey_code(n):
    a = [0 for _ in range(n + 1)]
    j = 0
    while True:
        yield a[n-1::-1]
        a[n] = 1 - a[n]
        if a[n] == 1:
            j = 0
        else:
            for i in range(n):
                if a[i] == 1:
                    j = i + 1
                    break
        if j >= n:
            return
        a[j] = 1 - a[j]


class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"{self.name} (Вес: {self.weight}, Стоимость: {self.value})"


def knapsack(items, capacity):
    n = len(items)
    max_value = 0
    best_combination = [0] * n
    current_weight = 0
    current_value = 0
    selected = [0] * n

    for code in grey_code(n):
        for i in range(n):
            if selected[i] != code[i]:
                if code[i] == 1:
                    current_weight += items[i].weight
                    current_value += items[i].value
                else:
                    current_weight -= items[i].weight
                    current_value -= items[i].value
                selected[i] = code[i]
                break
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
            best_combination = selected[:]

    return max_value, best_combination


if __name__ == '__main__':
    items = [
        Item("Предмет 1", weight=3, value=60),
        Item("Предмет 2", weight=2, value=100),
        Item("Предмет 3", weight=4, value=120)
    ]

    capacity = 5
    max_val, best_set = knapsack(items, capacity)

    print("Максимальная ценность:", max_val)
    print("Оптимальное состояние:", best_set)
    print("В оптимальном наборе:")
    for include, item in zip(best_set, items):
        if include:
            print(f"  {item}")
