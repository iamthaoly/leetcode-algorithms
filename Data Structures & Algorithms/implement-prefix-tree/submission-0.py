class PrefixTree:
    class Node:
        def __init__(self, val="", stop=False):
            self.val = val
            self.children = dict()
            self.stop = stop


    def __init__(self):
        self.root = self.Node()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            node = cur.children.get(word[i])
            if not node:
                node = self.Node(word[i])
                cur.children[word[i]] = node
            if i == len(word) - 1:
                node.stop = True
                
            cur = node


    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            node = cur.children.get(word[i])
            if not node:
                return False
            cur = node
            if i == len(word) - 1 and not cur.stop:
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
        
        