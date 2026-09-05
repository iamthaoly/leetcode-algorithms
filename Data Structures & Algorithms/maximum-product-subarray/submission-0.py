class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp_max = [None] * len(nums)
        dp_min = [None] * len(nums)
        
        dp_max[0] = dp_min[0] = res = nums[0]

        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], nums[i] * dp_max[i - 1], nums[i] * dp_min[i -1])
            dp_min[i] = min(nums[i], nums[i] * dp_max[i - 1], nums[i] * dp_min[i -1])
            res = max(res, dp_max[i])

        return res
            
