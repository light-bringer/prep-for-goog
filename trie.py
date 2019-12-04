from __future__ import print_function


# Python Trie implementation


class TrieNode(object):
    # Trie Node class
    # isEndOfWord represents end of word
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False


class Trie(object):

    # Trie data structure
    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        # returns trie node inited to Nones
        return TrieNode()
    
    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        lengthOfKey = len(key)

        for level in xrange(lengthOfKey):
            index = self._charToIndex(key[level])
            print(index)

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        
        pCrawl.isEndOfWord = True

    
    def isthisEndOfWord(self):
        return self.isEndOfWord


