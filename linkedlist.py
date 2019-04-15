from __future__ import print_function


class Node(object):

    def __init__(self, value=None):
        self.data = value
        self.next = None
    
    def print(self):
        print(self.data)
    
    def get_data(self):
        return self.data
    
    def set_data(self, val):
        self.data = val
    
    def get_next(self):
        return self.next
    
    def set_next(self, nextaddr):
        self.next = nextaddr
        


class LinkedList(object):
    
    def __init__(self):
        self.ll = []

    def insert(self, node):
        if 
