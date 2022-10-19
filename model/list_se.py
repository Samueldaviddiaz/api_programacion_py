from model.kid import Kid
from model.node import Node


class ListSE:
    def __init__(self):
        self.head = None
        self.size =0

    #0 = Contar
    def count(self):
        #Paso 1: Retorna el contador
        return self.count

    #1 = Adicionar al final
    def add(self, kid:Kid):
        #Paso 1: Si la cabeza está vacía:
        if self.head == None:
        #Paso 2: Nodo es la nueva cabeza
            self.head = Node(kid)
        else:
        #Paso 3: Sino, mientras hayan datos:
            temp = self.head
            while temp.next != None:
        #Paso 4: Temporal pásese
                temp = temp.next
        #Paso 5: Temporal, su siguiente es el nodo que se creó
            temp.next = Node(kid)
        #Paso 6: La talla crece 1
        self.size+=1

    #2 = Adicionar al inicio
    def add_to_start(self, kid:Kid):
        # Paso 1: Si la cabeza está vacía:
        if self.head == None:
        # Paso 2: Nodo es la nueva cabeza
            self.head = Node(kid)
        else:
        # Paso 3: Sino, se crea un nuevo nodo
            newNode = Node(kid)
        # Paso 4: Nuevo nodo, su siguiente será la que era antes la cabeza
            newNode.next = self.head
        # Paso 5: Nuevo nodo, ahora usted es la cabeza
            self.head = newNode
        # Paso 6: La talla crece 1
        self.size += 1

    #3 = Invertir
    def invert(self):
        if self.head != None:
        # Paso 1: Si la no cabeza está vacía:
            temp = self.head
        # Paso 2: Se crea una nueva lista
            newList = ListSE()
        # Paso 3: Mientras hayan datos:
            while temp != None:
        # Paso 4: Temporal, adicione los datos AL INICIO de la nueva lista
                newList.add_to_start(temp.data)
        # Paso 5: Temporal pásese
                temp = temp.next
        # Paso 6: Nueva lista, ahora su cabeza es la principal
            self.head = newList.head

    #4 = Primero niñas y luego niños
    def mix_by_gender(self):
        # Paso 1: Si el contador es diferente a 0 y es mayor que 1:
        if self.count != None and self.count > 1:
        # Paso 2: Se crea una lista copia
            new_list = ListSE
        # Paso 3: Se llama a temporal y se posiciona en la cabeza
            temp = self.head
        # Paso 4: Temporal, mientras hayan datos:
            while temp != None:
        # Paso 5: Temporal, si en los datos el género es "M":
                if temp.data.gender == 'M':
        # Paso 6: Adicione los datos a la nueva lista
                    new_list.add(temp.data)
                else:
        # Paso 7: Sino, adicione los datos AL INICIO de la nueva lista
                    new_list.add_to_start(temp.data)
        # Paso 8: Temporal pásese
                    temp = temp.next
        # Paso 9: Nueva lista, ahora su cabeza es la principal
                    ListSE.head = new_list.head
        # Paso 10: Retornar la nueva lista
        return new_list

    #5 = Adicionar por posición
    def add_by_position(self, position: int, kid: Kid):
        # Paso 1: Si la posición ingresada es 1:
        if position == 1:
        # Paso 2: Adicionar al inicio al niño
            self.add_to_start(kid)
        else:
        # Paso 3: Sino, creo un contador y llamo a temporal para que se posicione en la cabeza
            postemp = 1
            temp = self.head;
        # Paso 4: Mientras el temporal sea menor a la posición ingresada menos 1
            while postemp < (position - 1):
        # Paso 5: Temporal pásese y sume 1 al contador
                temp = temp.next
                postemp = postemp + 1
        # Paso 6: Creo un nuevo nodo
            newNode = Node(kid)
        # Paso 7: El nuevo nodo agarra al siguiente del temporal
            newNode.next = temp.next
        # Paso 8: Temporal, su siguiente es el nuevo nodo
            temp.next = newNode
        # Paso 9: La talla crece 1
            self.size += 1
