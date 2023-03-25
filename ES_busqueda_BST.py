class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)
    
    def search(self, valor):
        node = self.root
        return self.search_recur(node,valor)

    def search_recur(self, node, valor)-> bool:
        if node is not None:
            if node.value == valor:
                return True
            else:
                if node.value < valor:
                    return self.search_recur(node.right, valor)
                else:
                    return self.search_recur(node.left,valor)
        else:
            return False
