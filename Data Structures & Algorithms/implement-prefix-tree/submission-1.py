# Solution 2: Refactored few things

class PrefixTree:
    class Node:
        def __init__(self, val="", end_of_word=False):
            self.val = val
            self.children = dict()
            self.end_of_word = end_of_word

    def __init__(self):
        self.root = self.Node()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            node = cur.children.get(word[i])
            if not node:
                node = self.Node(word[i])
                cur.children[word[i]] = node
            cur = node

        cur.end_of_word = True


    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            node = cur.children.get(word[i])
            if not node:
                return False
            cur = node

        if not cur.end_of_word:
            return False

        return True
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            node = cur.children.get(prefix[i])
            if not node:
                return False
            cur = node
            
        return True
        
        