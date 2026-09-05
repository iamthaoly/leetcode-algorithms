class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]

        q = deque()
        res = 0

        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        fresh_all = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    fresh_all += 1
        
        while q:                        
            cells = len(q)
            has_fresh = False
            for _ in range(cells):
                cur = q.popleft()
                r, c = cur[0], cur[1]
                if not (0 <= r < row and 0 <= c < col and not visited[r][c] and grid[r][c] != 0):
                    continue
                visited[r][c] = True
                if grid[r][c] == 1:
                    has_fresh = True
                    fresh_all -= 1

                for m in moves:
                    q.append([r + m[0], c + m[1]])

            if has_fresh:
                res += 1

        if fresh_all > 0:
            return -1
        return res