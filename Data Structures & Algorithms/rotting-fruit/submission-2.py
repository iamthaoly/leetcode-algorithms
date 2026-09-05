class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]

        q = deque()
        res = 0

        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i, j])
        
        while q:                        
            cells = len(q)
            has_fresh = False

            for _ in range(cells):
                cur = q.popleft()
                r, c = cur[0], cur[1]
                visited[r][c] = True
                if grid[r][c] == 1:
                    has_fresh = True
                    grid[r][c] = 2

                for m in moves:
                    r2, c2 = r + m[0], c + m[1]
                    if 0 <= r2 < row and 0 <= c2 < col and not visited[r2][c2] and grid[r2][c2] != 0:
                        q.append([r2, c2])
            if has_fresh:
                res += 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1

        return res

