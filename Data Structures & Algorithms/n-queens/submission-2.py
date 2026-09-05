class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Solution 2: Backtracking (optimal)
        # Use set to check for checkmate
        # Time: O(n!)
        # Space: O(n^2)
        def process(i, j, add = True):
            if add:
                row.add(i)
                col.add(j)
                diag1.add(j - i)
                diag2.add(j + i)
            else:
                row.remove(i)
                col.remove(j)
                diag1.remove(j - i)
                diag2.remove(j + i)

        def backtrack(i, n):
            for j in range(n):
                if i in row or j in col or (j - i) in diag1 or (j + i) in diag2:
                    continue
                cur.append([i, j])
                process(i, j, True)
                if len(cur) == n:
                    queens.append(cur.copy())
                else:
                    backtrack(i + 1, n)
                cur.pop()
                process(i, j, False)
        cur = []
        queens = []
        row, col, diag1, diag2 = set(), set(), set(), set()
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

        
                