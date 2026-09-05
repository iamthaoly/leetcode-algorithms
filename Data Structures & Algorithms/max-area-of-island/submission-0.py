class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        visited = [[False for _ in range(col)] for _ in range(row)]

        def dfs(i, j):
            if not (0 <= i < row and 0 <= j < col) or visited[i][j]:
                return 0
            visited[i][j] = True
            if grid[i][j] == 0:
                return 0
            area = 1 + dfs(i, j - 1) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i - 1, j)
            return area

        res = 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j] == 1:
                    area = dfs(i, j)
                    res = max(res, area)
        return res