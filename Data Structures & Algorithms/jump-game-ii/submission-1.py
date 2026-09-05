class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        dp[len(nums) - 1] = 0
        for i in range(len(nums) - 2, -1, -1):
            min_j = float('inf')
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if dp[j] is not None:
                    min_j = min(min_j, dp[j])
            if min_j != float('inf'):
                dp[i] = 1 + min_j
        # print(dp)
        return dp[0]


