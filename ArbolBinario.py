class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def insertar(arbol, valor):
    if arbol == None:
        return Nodo(valor, None, None)
    if valor == arbol.valor:
        return Nodo(arbol.valor, arbol.izquierda, arbol.derecha)
    if valor > arbol.valor:
        return Nodo(arbol.valor, arbol.izquierda, insertar(arbol.derecha, valor))
    if valor < arbol.valor:
        return Nodo(arbol.valor, insertar(arbol.izquierda, valor), arbol.derecha)

def buscar(arbol, valor):
    if arbol == None:
        return False
    if arbol.valor == valor:
        return True
    if arbol.valor > valor:
        return buscar(arbol.izquierda, valor)
    return buscar(arbol.derecha, valor)

def insertar_lista(arbol, nodo_lista):
    if len(nodo_lista) == 1:
        return insertar(arbol, nodo_lista[0])
    return insertar_lista(insertar(arbol, nodo_lista[0]), nodo_lista[1::])

def a_lista(arbol):
    if arbol == None:
        return []
    return a_lista(arbol.izquierda) + [arbol.valor] + a_lista(arbol.derecha)

def print_arbol(arbol):
    if arbol != None:
        print_arbol(arbol.izquierda)
        print(arbol.valor)
        print_arbol(arbol.derecha)

arbol = Nodo(5, Nodo(3,None,None), Nodo(7,None,None))
#print_arbol(arbol)
arbol = insertar(arbol, 6)
#print_arbol(arbol)
#print(buscar(arbol, 6))
lista = [1 ,7, 8]
arbol = insertar_lista(arbol, lista)
#print_arbol(arbol)
Lista_dos = a_lista(arbol)
print(Lista_dos)
