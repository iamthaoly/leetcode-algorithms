class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if not (total % 2 == 0):
            return False
        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n, -1, -1):
            for j in range(target + 1):
                res = False
                if j == 0:
                    dp[i][j] = True
                    continue
                if i + 1 <= n:
                    res = dp[i + 1][j] 
                    if j - nums[i] >= 0:
                        res = res or dp[i + 1][j - nums[i]]
                dp[i][j] = res

        return dp[0][target]

        