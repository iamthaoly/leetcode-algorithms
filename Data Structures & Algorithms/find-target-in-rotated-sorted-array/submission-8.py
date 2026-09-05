class Solution:
    def find_pivot(self, nums):
        low, high = 0, len(nums) - 1
        mid = (low + high) // 2

        while low < high:
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
            mid = (low + high) // 2

        return low

    def binary_search(self, nums, target):
        low, high = 0, len(nums) - 1
        mid = (low + high) // 2
        while(low <= high):
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        if nums[pivot] <= target <= nums[len(nums) - 1]:
            res = self.binary_search(nums[pivot:], target)
            res += pivot if res != -1 else 0
            return res
        
        return self.binary_search(nums[:pivot], target)


