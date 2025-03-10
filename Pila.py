class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.siguiente=None

class Pila:
    def __init__(self):
        self.top=None
        self.size=0

    def push(self, dato):
        nuevoN=Nodo(dato)
        nuevoN.siguiente=self.top
        self.top=nuevoN
        self.size+=1
    
    def pop(self):
        if self.top == None:
            return None
        dato=self.top.dato
        self.top=self.top.siguiente
        self.size-=1
        return dato
    
    def get_top(self):
        return self.top.dato if self.top else None
    
    def get_size(self):
        return self.size
    
"""pila=Pila()
pila.push("Jesus")  
pila.push("Maria")
pila.push("Jose")
print("Size->",pila.get_size())  #3
print("Top ->",pila.get_top())   #Jose
print("Pop ->",pila.pop())       #Jose
print("Top ->",pila.get_top())   #Maria
print("Pop ->",pila.pop())       #Maria
print("Pop ->",pila.pop())       #Jesus
print("Pop ->",pila.pop())       #None
print("Top ->",pila.get_top())   #None
print("Size->",pila.get_size())  """#0
