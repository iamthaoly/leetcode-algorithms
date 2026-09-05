class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # PRACTICE MODE
        def dfs(i, j):
            # Check conditions
            if not (0 <= i < row and 0 <= j < col and not visited[i][j] and grid[i][j] == "1"):
                return
            
            visited[i][j] = True
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        row = len(grid)
        col = len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    count += 1
        
        return count
