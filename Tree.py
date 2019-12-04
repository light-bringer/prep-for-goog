class TreeNode(object):

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
    
    def setLeftchild(self, newLeftNode):
        self.left = newLeftNode
    
    def setRightchild(self, newRightNode):
        self.left = newRightNode



class Tree(object):
    def __init__(self):
        self.tree = None
    
    def setInOrderTraversal(self, listOfValues):
        pass
    
    def setPreOrderTraversal(self, listOfValues):
        pass
    
    def setPostOrderTraversal(self, listOfValues):
        pass
    
    
    
    def getPreOrderTraversal(self):
        pass
    
    def getPostOrderTraversal(self):
        pass



a = Tree()
a.getPreOrderTraversal()
a.getPostOrderTraversal()
a.getInOrderTraversal()






