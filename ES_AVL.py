class NodeAVL:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    # Método para obtener la altura del árbol
    def height(self, node):
        if node is None:
            return 0
        return node.height

    # Método para obtener el factor de equilibrio del nodo
    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Método para realizar una rotación hacia la derecha
    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        new_root.height = max(self.height(new_root.left), self.height(new_root.right)) + 1
        return new_root

    # Método para realizar una rotación hacia la izquierda
    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        new_root.height = max(self.height(new_root.left), self.height(new_root.right)) + 1
        return new_root

    # Método para insertar un nodo en el árbol AVL
    def insert(self, val):
        # Función recursiva para insertar un nodo
        def _insert(node, val):
            # Si el nodo es nulo, se crea un nuevo nodo con el valor dado
            if node is None:
                return NodeAVL(val)

            # Si el valor es menor que el valor del nodo actual, se inserta en el subárbol izquierdo
            if val < node.val:
                node.left = _insert(node.left, val)

            # Si el valor es mayor que el valor del nodo actual, se inserta en el subárbol derecho
            elif val > node.val:
                node.right = _insert(node.right, val)

            # Si el valor ya existe en el árbol, no se inserta nada
            else:
                return node

            # Se actualiza la altura del nodo actual
            node.height = max(self.height(node.left), self.height(node.right)) + 1

            # Se verifica el factor de equilibrio del nodo actual
            balance = self.balance_factor(node)
    
            # Si el factor de equilibrio es mayor que 1, significa que el subárbol izquierdo es más alto
            # que el subárbol derecho y se necesita una rotación hacia la derecha
            if balance > 1 and val < node.left.val:
                # Si el valor a insertar es menor que el valor del subárbol izquierdo, significa que
                # se necesita una rotación simple hacia la derecha
                return self.rotate_right(node)

            # Si el factor de equilibrio es menor que -1, significa que el subárbol derecho es más alto
            # que el subárbol izquierdo y se necesita una rotación hacia la izquierda
            elif balance < -1 and val > node.right.val:
                # Si el valor a insertar es mayor que el valor del
                return self.rotate_left(node)
            
            elif balance > 1 and val > node.left.val:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            
            elif balance<-1 and val < node.right.val:
                node.right = self.rotate_right(node)
                return self.rotate_left(node)
            
            return node
        
    # Método para realizar una búsqueda en el árbol AVL
    def search(self, val):
        # Función recursiva para buscar un valor en un subárbol
        def _search(node, val):
            # Si el nodo es nulo, el valor no se encuentra en el árbol
            if node is None:
                return None

            # Si el valor es menor que el valor del nodo actual, se busca en el subárbol izquierdo
            if val < node.val:
                return _search(node.left, val)

            # Si el valor es mayor que el valor del nodo actual, se busca en el subárbol derecho
            elif val > node.val:
                return _search(node.right, val)

            # Si el valor es igual al valor del nodo actual, se devuelve el nodo
            else:
                return node

        # Se llama a la función recursiva con la raíz del árbol
        return _search(self.root, val)