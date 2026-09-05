class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(i, n):
            for j in range(n):
                checkmate = False
                for x, y in cur:
                    if i == x or j == y or (j - i == y - x) or (j + i == y + x):
                        checkmate = True
                        break
                if not checkmate:
                    cur.append([i, j])
                    if len(cur) == n:
                        queens.append(cur.copy())
                    else:
                        backtrack(i + 1, n)
                    cur.pop()
        cur = []
        queens = []
        backtrack(0, n)

        res = []
        for p in queens:
            # Mistake 2
            # board = [("." * n)] * n
            board = [["." for _ in range(n)] for _ in range(n)]
            for i, j in p:
                board[i][j] = "Q"
            res.append(["".join(x) for x in board])

        return res

        
                