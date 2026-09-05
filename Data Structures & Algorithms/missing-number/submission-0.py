class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Solution: Optimal space O(1)
        # Using XOR
        xorr = len(nums)
        for i in range(len(nums)):
            xorr = xorr ^ (i ^ nums[i])
        return xorr