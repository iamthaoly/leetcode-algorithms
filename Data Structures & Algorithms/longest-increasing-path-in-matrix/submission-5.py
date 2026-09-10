class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal row, col
            if (i, j) in visited:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            visited.add((i, j))

            moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            max_path_len = 0
            for mx, my in moves:
                next_i, next_j = i + mx, j + my
                if 0 <= next_i < row and 0 <= next_j < col and (next_i, next_j) not in visited and matrix[next_i][next_j] > matrix[i][j]:
                    max_path_len = max(max_path_len, dfs(next_i, next_j))
            max_path_len += 1

            visited.remove((i, j))
            dp[(i, j)] = max_path_len
            return max_path_len
        
        row, col = len(matrix), len(matrix[0])
        res = 0
        dp = {}
        for i in range(row):
            for j in range(col):
                visited = set()
                res = max(res, dfs(i, j))
        
        return res
