class Node:
    def __init__(self, data, color='R'):
        self.data = data
        self.color = color  
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color='B')  
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'R'
        self.fix_insert(new_node)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, node):
        while node.parent and node.parent.color == 'R':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'R':  
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.right: 
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'B'  
                    node.parent.parent.color = 'R'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'B'

    def inorder_traversal(self, node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            print(node.data, node.color, end=' | ')
            self.inorder_traversal(node.right)

    def print_tree(self):
        self.inorder_traversal(self.root)
        print()

def create_tree_with_data(data_list):
    rbt = RedBlackTree()
    for data in data_list:
        rbt.insert(data)
    return rbt
