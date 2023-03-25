import random 
import time
import matplotlib.pyplot as plt
from ES_busqueda_BST import BST
from ES_AVL import AVLTree

random.seed(2122)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def show(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def sort(self):
        if self.head is None:
            return
        current_node = self.head
        sorted_list = None

        while current_node is not None:
            next_node = current_node.next

            if sorted_list is None or current_node.value < sorted_list.value:
                current_node.next = sorted_list
                sorted_list = current_node
            else:
                current_sorted_node = sorted_list
                while current_sorted_node.next is not None and current_sorted_node.next.value < current_node.value:
                    current_sorted_node = current_sorted_node.next
                current_node.next = current_sorted_node.next
                current_sorted_node.next = current_node

            current_node = next_node

        self.head = sorted_list
    
    # Método para buscar un valor en la lista enlazada utilizando búsqueda binaria
    def binary_search(self, value):
        left = 0
        right = self.length() - 1
        while left <= right:
            middle = (left + right) // 2
            current_node = self.get_node(middle)
            if current_node.value == value:
                return middle
            elif current_node.value < value:
                left = middle + 1
            else:
                right = middle - 1
        return -1

    def busqueda_binaria(self, valor_buscado):
        inicio = 0
        fin = self.length() - 1
        encontrado = False
        while inicio <= fin and not encontrado:
            mitad = (inicio + fin) // 2
            nodo_actual = self.head
            for i in range(mitad):
                nodo_actual = nodo_actual.next
            if nodo_actual.value == valor_buscado:
                encontrado = True
            else:
                if valor_buscado < nodo_actual.value:
                    fin = mitad - 1
                else:
                    inicio = mitad + 1
        return encontrado

    def length(self):
        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length
    
    def get_node(self, index):
        current_node = self.head
        current_index = 0
        while current_node is not None and current_index < index:
            current_node = current_node.next
            current_index += 1
        return current_node

    def search(self, value):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1
        return -1
    

if __name__=='__main__': 
    # crear una lista enlazada simple y agregar algunos nodos
    my_list = LinkedList()

    # Crear una lista de tamnaño 500 con numeros aleatorios
    list_number_random = random.sample(range(1, 100000), 500) 

    for value in list_number_random:
        my_list.add_node(value=value)

    # buscar un valor en la lista
    index = my_list.search(-1)
    if index == -1:
        print("El valor no se encontró")
    else:
        print(f"El valor se encontró en la posición {index}")

    # mostrar la lista sin ordenar
    #my_list.show()

    # ordenar la lista y mostrarla
    my_list.sort()

    list1_value_search = [30, 43545, 34, 488, 993, -1]
    list2_value_search = [30, 43545, 34, 488, 993, -1, 3489, 122, 23, 674, 2, 18]
    list3_value_search = [30, 43545, 34, 488, 993, -1, 3489, 122, 23, 674, 2, 18, 84, 1, 7, 483, 21, 90]
    list4_value_search = [30, 43545, 34, 488, 993, -1, 3489, 122, 23, 674, 2, 18, 84, 1, 7, 483, 21, 90, 125, 37, 86, 23, -100, 9999]

    lista_all = [list1_value_search, list2_value_search, list3_value_search, list4_value_search]

    # Variable para guardar el tiempo de busqueda
    list_time_search_LinkedList = []

    for list_value in lista_all:
        start_time = time.time()
        for value in list_value:
            print(my_list.busqueda_binaria(value))
        end_time = time.time()
        time_search = (end_time - start_time)*1000
        list_time_search_LinkedList.append(time_search)
        print(time_search)


    # Line for BST
    # crear una instancia de la clase BST y agregar algunos valores
    my_bst = BST()
    # Insertar datos en el BST
    for value in list_number_random:
        my_bst.insert(value=value)

    # Lista para almacenar los tiempos de busqueda en BST
    list_time_search_bst = []
    # Realizamos la busqueda del arbol binario
    for list_value in lista_all:
        start_time_bst = time.time()
        for value in list_value:
            print(my_bst.search(valor=value))
        end_time_bst = time.time()
        print((end_time_bst-start_time_bst)*1000)
        list_time_search_bst.append((end_time_bst-start_time_bst)*1000)

    
    # Line for AVL
    my_avl = AVLTree()
    # Insertar datos
    for value in list_number_random:
        my_avl.insert(val=value)

    # Lista para guardar os tiempos de busqueda en AVL
    list_time_search_avl = []
    for list_value in lista_all:
        start_time_avl = time.time()
        for value in list_value:
            print(my_avl.search(val=value))
        end_time_avl = time.time()
        print((end_time_avl-start_time_avl)*1000)
        list_time_search_avl.append((end_time_avl-start_time_avl)*1000)

    # Graficamos con matplotlib de lista simple y BST
    fig, ax = plt.subplots()
    x_value = [6, 12, 18, 24]
    ax.plot(x_value, list_time_search_LinkedList, label=  'LinkedList')
    ax.scatter(x_value, list_time_search_LinkedList)
    ax.plot(x_value, list_time_search_bst, label = 'BST')
    ax.scatter(x_value, list_time_search_bst)
    ax.plot(x_value, list_time_search_avl, label = 'AVL')
    ax.scatter(x_value, list_time_search_avl)
    ax.set_xticks(x_value)  # establecer los ticks del eje x
    ax.set_title("Busqueda de BST y LinkedList")
    ax.set_xlabel("Tamaño de lista")
    ax.set_ylabel("Time [ms]")
    lista = []
    for sublista in [list_time_search_LinkedList, list_time_search_bst, list_time_search_avl]:
        lista.extend(sublista)
    plt.yticks(lista) # Establecer los valores y las etiquetas del eje Y
    plt.legend()
    plt.grid()
    plt.show()
