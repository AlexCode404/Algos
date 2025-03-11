import time

class Node:
    def __init__(self, value):
        self.value = value  
        self.left = None    
        self.right = None   

def insert_node(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    return root

def in_order_traversal(root):
    if root is None:
        return []
    return in_order_traversal(root.left) + [root.value] + in_order_traversal(root.right)

def tree_sort(arr):
    root = None
    for num in arr:
        root = insert_node(root, num)
    return in_order_traversal(root)


test_strings = [
    "яблоко", "банан", "киви", "апельсин", "манго", "груша", "виноград",
    "персик", "ананас", "слива", "черешня", "арбуз", "дыня", "малина",
    "ежевика", "смородина", "лимон", "лайм", "авокадо", "финик", "инжир",
    "абрикос", "нефрит", "мята", "орех", "кокос"
]

start_time = time.time()
print("\nСортировка большого списка строк:")
print(tree_sort(test_strings))
end_time = time.time()
print(f"Время выполнения: {end_time - start_time:.6f} секунд")
