class Solution:
    class TrieNode:
        def __init__(self, char):
            self.char = char
            self.children = {}
            self.ending = False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def add_to_trie(word, root):
            for char in word:
                if char not in root.children:
                    root.children[char] = self.TrieNode(char)
                root = root.children[char]
            root.ending = True

        def backtrack(i, j, node):
            nonlocal row, col
            if not (0 <= i < row and 0 <= j < col and board[i][j] != "#"):
                return
            if board[i][j] not in node.children:
                return

            char = board[i][j]
            child = node.children[char]
            board[i][j] = "#"

            path.append(char)
            if child.ending:
                res.add("".join(path))
                
            backtrack(i, j - 1, child)
            backtrack(i, j + 1, child)
            backtrack(i - 1, j, child)
            backtrack(i + 1, j, child)

            # reset state
            board[i][j] = char
            path.pop()

        row, col = len(board), len(board[0])
        root = self.TrieNode("")
        path, res = [], set()

        for word in words:
            add_to_trie(word, root)

        for i in range(row):
            for j in range(col):
                backtrack(i, j, root)

        return list(res)
        
        