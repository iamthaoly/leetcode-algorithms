class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Mistakes
        #  - Forgot the approach
        def dfs(k, i, j) -> bool:
            # base case - compare
            if not (0 <= i < row and 0 <= j < col and (i, j) not in visited and board[i][j] == word[k]):
                return False
            visited.add((i, j))
            # cur.append(word[k])
            if k == len(word) - 1:
                return True
            res = (dfs(k + 1, i, j - 1) or 
                    dfs(k + 1, i, j + 1) or
                    dfs(k + 1, i - 1, j) or
                    dfs(k + 1, i + 1, j))
            
            # cur.pop()
            visited.remove((i, j))
            return res

        
        row, col = len(board), len(board[0])
        # cur = []
        for i in range(row):
            for j in range(col):
                # cur = []
                visited = set()
                if dfs(0, i, j):
                    return True
        
        return False
