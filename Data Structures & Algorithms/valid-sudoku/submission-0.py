class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        box = defaultdict(set)

        for i in range(N):
            for j in range(N):
                num = board[i][j]
                if num == ".":
                    continue
                if num in rows[i] or num in cols[j] or num in box[(i // 3, j // 3)]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                box[(i // 3, j // 3)].add(num)
        
        return True