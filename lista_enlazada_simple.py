class Estudiantes:
    def __init__(self, name = None, id = None, course = None):
        self.name = name
        self.id = id
        self.course = course

    def __str__(self):
        return self.name + " " + self.id + " " + self.course

class Nodo:
    def __init__(self, estudiante = None):
        self.estudiante = estudiante
        self.next = None
    
    def __str__(self):
        return f"{self.estudiante}"
    
class Listasimple:
    def __init__(self):
        self.head = None
     
    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            aux_node = self.head
            while aux_node.next is not None:
                aux_node = aux_node.next          
            aux_node.next = new_node

    def remove_head(self):
        self.head = self.head.next

    def remove_last_head(self):
        if self.head.next is None:
            self.head = None
        else:
            aux_node = self.head
            while aux_node.next.next is not None:
                aux_node = aux_node.next
            
            ultimo_node = aux_node.next
            ultimo_node = None
            aux_node.next = None

    def remove_index(self):
        pass

    def display(self):
        aux_node = self.head
        while aux_node is not None:
            print(aux_node)
            aux_node = aux_node.next
        

if __name__=='__main__':

    lista_simple = Listasimple()

    while True:
        print("\n------Menu------- \n"+
        "[1] Insert. \n" +
        "[2] Remove a node for index. \n" +
        "[3] Display \n" +
        "[4] Remove head node \n" +
        "[5] Remove last node \n" +
        "[x] Exit")
        option = input("Enter the option: ")

        if option == '1':
            name = input("Enter your name: ")
            id = input("Enter your id: ")
            course = input("Enter your course: ")
            estudiante = Estudiantes(name=name, id=id, course=course)
            node = Nodo(estudiante=estudiante)
            lista_simple.insert(node)

        elif option == '2':
            pass
        elif option == '3':
            lista_simple.display()

        elif option == '4':
            lista_simple.remove_head()
        
        elif option == '5':
            lista_simple.remove_last_head()

        elif option.lower() == 'x':
            break
    
