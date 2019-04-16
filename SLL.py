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
        



class LengthMetaclass(type):

    def __len__(self):
        return self.clslength()

class SingleLinkedList(object):

    __metaclass__ = LengthMetaclass
    
    def __init__(self):
        self.ll = None
        self.size = 0

    def insert(self, value):
        node = Node(value)
        if self.ll:
            temp = self.ll
            while temp.next:
                temp = temp.next
            temp.next  = node        
        else:
            self.ll = node
        
        self.size += 1
            
    
    def print(self):
        temp = self.ll
        while temp:
            print(temp.get_data() + " -> " )
            temp = temp.get_next()
    
    def __len__(self):
        return self.size


    def search(self, value):
        counter = 0
        temp = self.ll
        found = False
        while temp:
            if temp.get_data() == value:
                print("data found at index: {0}".format(counter))
                found = True
            counter += 1
            temp = temp.next
        if found:
            print("Found")
        else:
            print("Not Found..")


abc = SingleLinkedList()
abc.insert(2)
abc.insert(21)
abc.insert("hi")


abc.print()
print(len(abc))
abc.search("hi")