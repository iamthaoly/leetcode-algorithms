class WordDictionary:
    class Node:
        def __init__(self, char):
            self.char = char
            self.ending = False
            self.children = {}
            self.chars = set()

    def __init__(self):
        self.root = self.Node("")
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.chars:
                node = self.Node(char)
                cur.children[char] = node
                cur.chars.add(char)
            cur = cur.children[char]
        cur.ending = True

    def search(self, word: str) -> bool:
        # Mistakes:
        # - ["dog"],["do.."] This case
        # - This case [".."] should limit to 2 CHARS!!
        def dfs(i, cur: Node):
            # if i == len(word) - 1:
            #     if word[i] == ".":
            #         return len(cur.children) > 0
            #     else:
            #         return (word[i] in cur.chars) and cur.children[word[i]].ending
            if i >= len(word):
                return cur.ending  

            if word[i] != ".":
                if word[i] in cur.chars:
                    return dfs(i + 1, cur.children[word[i]])
            else:

                for _, node in cur.children.items():
                    if dfs(i + 1, node):
                        return True
            
            return False

        return dfs(0, self.root)
        
