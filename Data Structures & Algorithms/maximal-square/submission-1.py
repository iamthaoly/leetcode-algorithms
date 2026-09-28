class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def get_width() -> int:
            width = 0
            nonlocal row, col

            while q:
                size = len(q)
                # print(size)
                if size != (width + 1) ** 2 - width ** 2:
                    return width
                for _ in range(size):
                    x, y = q.popleft()
                    # if matrix[x][y] == '0':
                    #     return width
                    for mx, my in moves:
                        x2, y2 = x + mx, y + my
                        if 0 <= x2 < row and 0 <= y2 < col and (x2, y2) not in visited and matrix[x2][y2] == '1':
                            q.append([x2, y2])
                            visited.add((x2, y2))
                width += 1
            return width

        row, col = len(matrix), len(matrix[0])
        visited = set()
        max_width = 0
        moves = [[0, 1], [1, 0], [1, 1]]

        for i in range(row):
            for j in range(col):
                # if matrix[i][j] == '1' and (i, j) not in visited:
                if matrix[i][j] == '1':
                    visited = set()
                    q = deque([[i, j]])
                    visited.add((i, j))
                    max_width = max(max_width, get_width())

        return max_width * max_width

