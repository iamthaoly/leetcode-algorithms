class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, cur):
            if cur == len(word):
                return True

            if not (0 <= i < len(board) and 0 <= j < len(board[i]) and 
                visited[i][j] == False and board[i][j] == word[cur]):
                return False

            visited[i][j] = True

            res = (dfs(i, j + 1, cur + 1) or 
                   dfs(i, j - 1, cur + 1) or
                   dfs(i + 1, j, cur + 1) or
                   dfs(i - 1, j, cur + 1))
            visited[i][j] = False
            return res

        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                visited = [[False for _ in range(cols + 1)] for _ in range(rows + 1)]
                if dfs(i, j, 0):
                    return True
        return False