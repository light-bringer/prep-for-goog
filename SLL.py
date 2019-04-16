from __future__ import print_function


class Node(object):

    def __init__(self, value=None):
        self.data = value
        self.next = None
    
    def print(self):
        print(self.data)
    
    def get_data(self):
        return str(self.data)
    
    def set_data(self, val):
        self.data = val
    
    def get_next(self):
        return self.next
    
    def set_next(self, nextaddr):
        self.next = nextaddr
        


class SingleLinkedList(object):
    
    def __init__(self):
        self.ll = None

    def insert(self, value):
        node = Node(value)
        if self.ll:
            temp = self.ll
            while temp.next:
                temp = temp.next
            temp.next  = node        
        else:
            self.ll = node
            
    
    def print(self):
        temp = self.ll
        while temp:
            print(temp.get_data() + " -> " )
            temp = temp.get_next()


abc = SingleLinkedList()
abc.insert(2)
abc.insert(21)
abc.insert("hi")

abc.print()