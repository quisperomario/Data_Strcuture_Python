#TODO: ESTRUCTURA DE DATOS -> Tabla Hash
def funcion_hash(clave):
    valor  = 0
    for letra in clave:
        valor += ord(letra)
    return valor

def lista_buscar(lista, predicado):
    for elemento in lista:
        if predicado(elemento):
            return elemento
    return None

class Par:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor

class Hash:
    def __init__(self, capacidad):
        self.capacidad = max(capacidad, 3)
        self.tabla = [[] for x in range(self.capacidad)]
        self.cantidad = 0
    
    def insertar(self, clave, valor):
        posicion = funcion_hash(clave)%self.capacidad 
        lista = self.tabla[posicion]
        par_existente = lista_buscar(lista, lambda x: x.clave == clave)

        if par_existente:
            par_existente.valor = valor
        else:
            lista.append(Par(clave, valor))

    def buscar(self, clave):
        posicion = funcion_hash(clave)%self.capacidad 
        lista = self.tabla[posicion]
        par_existente = lista_buscar(lista, lambda x: x.clave == clave)

        print("par_existente = ", par_existente)
        return par_existente.valor if par_existente else None
    
    #TODO: override del metodo
    def __str__(self):
        texto = "{\n"
        for lista in self.tabla:
            for elemento in lista:
                texto += " " + str(elemento.clave) + " " + str(elemento.valor) + "\n" 
        texto += "}\n" 
        return texto

    def __getitem__(self, key):
        return self.buscar(key)

    def __setitem__(self,key , value):
        self.insertar(key, value)
 

if __name__ == "__main__":

    h = Hash(5)
    h.insertar("romario", 24)
    h.insertar("smith", 22)
    h.insertar("yovana", 19)
    print(h)
    print(h["romario"])
    h["romario"] = 100
    print(h)

