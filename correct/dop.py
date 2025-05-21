def find_min_max(sequence):
    if len(sequence) == 0:
        return [0, 0]
    min_max = [sequence[0], sequence[0]]
    for element in sequence:
        if element < min_max[0]:
            min_max[0] = element
        if element > min_max[1]:
            min_max[1] = element
    return min_max

def counting_sort(sequence):
    # вместо min(sequence) и max(sequence) используем нашу функцию
    min_value, max_value = find_min_max(sequence)

    support = [0 for _ in range(max_value - min_value + 1)]
    for element in sequence:
        support[element - min_value] += 1

    index = 0
    for i in range(len(support)):
        for _ in range(support[i]):
            sequence[index] = i + min_value
            index += 1
    return None

# Пример
sequence = [5, 0, -2, 7, 3, -2]
print("До:", sequence)
counting_sort(sequence)
print("После:", sequence)
