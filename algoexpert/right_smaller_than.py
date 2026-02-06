def rightSmallerThan(array):
    count = []
    root = None
    for num in reversed(array):
        node = BSTNode(num)
        root = insert(root, node)
        count.append(node.right_smaller_num)
    return count[::-1]

def insert(parent, node):
    if parent is None:
        return node
    if node.value > parent.value:
        node.right_smaller_num += parent.left_tree_size + 1
        parent.right = insert(parent.right, node)
    else:
        parent.left_tree_size += 1
        parent.left = insert(parent.left, node)
    return parent

class BSTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.right_smaller_num = 0
        self.left_tree_size = 0
        self.value = value
        
