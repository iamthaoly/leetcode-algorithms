class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Solution 2: Dijkstra (Optimized)
        # Time: O((n^2) * log(n))
        # Space: O(n^2)
        n = len(grid)
        visited = [[False for _ in range(n)] for _ in range(n)]
        min_heap = [[grid[0][0], 0, 0]]

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
                    temp = max(t, grid[x][y])
                    heapq.heappush(min_heap, [temp, x, y])
        return 0

