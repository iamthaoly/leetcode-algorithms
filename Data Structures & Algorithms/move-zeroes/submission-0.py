class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 # next non 0 
        # Copy non 0 to first part
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
        
        print(nums)
        # Fill the remaining part with 0
        while l < len(nums):
            nums[l] = 0
            l += 1

        # print(nums)

        # k = 0
        # for i, val in enumerate(nums):
        #     if val != 0:
        #         nums[i], nums[k] = nums[k], val
        #         k += 1

