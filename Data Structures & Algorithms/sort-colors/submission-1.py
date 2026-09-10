class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 2: Two pointers

        # Move 0
        left = len(nums) - 1
        for right in range(len(nums) - 1, -1, -1):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left -= 1

        # print(nums, left)
        left = len(nums) - 1
        for right in range(len(nums) - 1, -1, -1):
            if nums[right] != 1 and nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left -= 1
        
        # print(nums)




