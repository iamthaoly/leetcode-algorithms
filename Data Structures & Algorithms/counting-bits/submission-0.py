class Solution:
    def countBits(self, n: int) -> List[int]:
        # Solution 1: obvious one
        res = []

        for i in range(0, n + 1):
            cur = i
            count = 0
            while (cur > 0):
                count += 1
                cur = cur & (cur - 1)
            res.append(count)

        return res