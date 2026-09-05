class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None] * n

        def solve2(i, j):
            nonlocal n
            if i >= n:
                return 0

            r1 = solve(i + 1, j) # not include nums[i]
            r2 = 0
            if j == -1 or nums[i] > nums[j]:
                r2 = 1 + solve(i + 1, i) # include nums[i]
            
            return max(r1, r2)

        def solve(i):
            nonlocal n
            if i >= n:
                return 0
            if dp[i]:
                return dp[i]

            res = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    res = max(res, 1 + solve(j))
            dp[i] = res
            return dp[i]

        res = 0
        for i in range(n):
            res = max(res, solve(i))
            
        return res

