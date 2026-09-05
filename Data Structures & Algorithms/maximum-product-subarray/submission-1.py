class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # dp_max = [None] * len(nums)
        # dp_min = [None] * len(nums)
        
        dp_max = dp_min = res = nums[0]

        for i in range(1, len(nums)):
            val = nums[i]
            mx, mn = dp_max, dp_min
            dp_max = max(val, val * mx, val * mn)
            dp_min = min(val, val * mx, val * mn)
            res = max(res, dp_max)

        return res
            
