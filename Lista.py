from No import No

class Lista:
    def __init__(self):
        self.initial  = None
        self.size = 0
        self.end = None

    def append(self, data):
        if self.initial:
            pointer = self.initial
            while pointer.next:
                pointer = pointer.next
            pointer.next = No(data, pointer)
            self.end = pointer.next
        else:
            self.initial = No(data, None)
            self.end = self.initial
        self.size += 1

    def print(self):
        if self.initial == None:
            print("Lista vazia")
        else:
            pointer = self.initial
            while pointer:
                print(pointer.data)
                pointer = pointer.next
            print("Tamanho da lista: ", self.size)

    def printinverse(self):
        if self.end == None:
            print("Lista vazia")
        else:
            pointer = self.end
            while pointer:
                print(pointer.data)
                pointer = pointer.previous
            print("Tamanho da lista: ", self.size)
