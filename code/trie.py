class TrieNode:

    def __init__(self):
        self.children = {}
        self.isLeaf = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def get_children(self, ch):
        return self.root.children[ch]
    
    def insert(self, word):

        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        
        curr.isLeaf = True
    
    def search(self, word):
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]

        return curr.isLeaf

    def startWith(self, prefix):

        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        
        return True






    