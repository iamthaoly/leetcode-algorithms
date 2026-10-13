class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        smallest = None
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                smallest = i
                break

        if smallest is None:
            return nums.sort()

        bigger = None
        for i in range(smallest + 1, len(nums)):
            if not bigger or (nums[i] > nums[smallest] and nums[i] < nums[bigger]):
                bigger = i
        
        nums[smallest], nums[bigger] = nums[bigger], nums[smallest]
        nums[smallest + 1:] = reversed(nums[smallest + 1:])

        return nums

        