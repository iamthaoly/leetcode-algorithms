class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(i):
            if i == len(digits):
                res.append("".join(cur))
                return

            d = int(digits[i])
            for ch in nums[d]:
                cur.append(ch)
                backtrack(i + 1)
                cur.pop()

        if not digits:
            return []
        nums = [[] for _ in range(10)]
        ch = 'a'
        for i in range(2, 10):
            k = 4 if (i == 7 or i == 9) else 3
            for j in range(k):
                nums[i].append(ch)
                ch = chr(ord(ch) + 1)
        cur = []
        res = []
        backtrack(0)
        return res
        