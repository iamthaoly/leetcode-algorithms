class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        time = [[float('inf') for _ in range(n)] for _ in range(n)]
        visited = [[False for _ in range(n)] for _ in range(n)]
        time[0][0] = grid[0][0]
        min_heap = [[time[0][0], 0, 0]]

        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while min_heap:
            t, i, j = heapq.heappop(min_heap)
            if i == n - 1 and j == n - 1:
                return t
            if visited[i][j]:
                continue
            visited[i][j] = True
            for m in moves:
                x, y = i + m[0], j + m[1]
                if x >= 0 and x < n and y >= 0 and y < n and not visited[x][y]:
                    temp = max(time[i][j], grid[x][y])
                    # if temp < time[x][y]:
                    time[x][y] = temp
                    heapq.heappush(min_heap, [temp, x, y])
        # print(time)
        return time[n - 1][n - 1]

