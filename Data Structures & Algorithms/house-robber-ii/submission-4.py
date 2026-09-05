class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # not count last one
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        res = max(dp[0], dp[1])
        if len(nums) == 2:
            return res

        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            res = max(res, dp[i])
        print(dp)

        # not count first one
        dp = [0] * len(nums)
        dp[0] = nums[1]
        dp[1] = max(nums[2], nums[1])
        res = max(res, dp[1])
        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 1], nums[i + 1] + dp[i - 2])
            res = max(res, dp[i])
        print(dp)
        return res

