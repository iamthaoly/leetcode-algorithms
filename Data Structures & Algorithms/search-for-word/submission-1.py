class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        def should_visit(visited, i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[i]) and visited[i][j] == False

        def dfs(i, j, cur):
            nonlocal s
            if s == word:
                return True

            s += board[i][j]
            visited[i][j] = True
            if s[cur] != word[cur]:
                return False
            if s == word:
                return True

            for m in moves:
                if should_visit(visited, i + m[0], j + m[1]):
                    r = dfs(i + m[0], j + m[1], cur + 1)
                    if r:
                        return True
                    s = s[:-1]
                    visited[i + m[0]][j + m[1]] = False


            return False

        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(board)
        cols = len(board[0])
        # board = board[0]
        for i in range(rows):
            for j in range(cols):
                visited = [[False for _ in range(cols + 1)] for _ in range(rows + 1)]
                # print(visited)
                s = ""
                # cur = 0
                if dfs(i, j, 0):
                    return True
        return False
        