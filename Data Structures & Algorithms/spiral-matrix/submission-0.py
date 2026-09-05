class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        q = deque(deque(row) for row in matrix)
        res = []
        # Solution: optimal
        # Use deque
        # Travel by: top row, right col, bottom row, left col
        # Bottom row and left col: reverse
        while q:
            # Top row
            res += list(q.popleft())
            # Right column
            if q and q[0]:
                for row in q:
                    res.append(row.pop())
            # Bottom row
            if q:
                res += reversed(list(q.pop()))
            # Left column
            if q and q[0]:
                for row in reversed(q):
                    res.append(row.popleft())
        return res
