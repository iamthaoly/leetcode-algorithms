class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        visited = [[False for _ in range(col)] for _ in range(row)]
        # print(visited)

        def dfs(i, j):
            if not (0 <= i < row and 0 <= j < col) or visited[i][j]:
                return
            visited[i][j] = True
            if grid[i][j] == "0":
                return
            
            # 4 directions
            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i - 1, j)
            # if count area
            # return sum of above 

        count = 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count

        