class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mx = [None] * len(nums)
        # mn = [None] * len(nums)
        mx[0] = max(nums[0], float('-inf'))
        # mn[0] = min(nums[0], 0)
        res = mx[0]

        for i in range(1, len(nums)):
            mx[i] = max(nums[i] + mx[i - 1], nums[i])
            # mn[i] = min(nums[i] + mx[i - 1], nums[i] + mn[i - 1], nums[i], 0)
            res = max(res, mx[i])

        return res
