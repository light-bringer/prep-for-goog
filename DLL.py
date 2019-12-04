from __future__ import print_function

# Double Linked List Implementation
# DLL insert/search/print/delete

class DLLNode(object):

    def __init__(self, value=None, previous=None, following=None):
        self.data = value
        self.prev = previous
        self.next = following


class DLL(object):

    def __init__(self):
        self.dll = None

    def insert(self, data):
        node = DLLNode(value=data)
        if self.dll:
            pass
        else:
            self.dll = node