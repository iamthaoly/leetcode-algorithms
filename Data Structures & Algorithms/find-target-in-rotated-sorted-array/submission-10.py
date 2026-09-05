class Solution:
    # PRACTICE
    # Solution 2 (cleaner)
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums):
            low, high = 0, len(nums) - 1

            while low < high:
                mid = (low + high) // 2
                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid

            return low

        def binary_search(low, high):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        
        pivot = find_pivot(nums)
        if nums[pivot] <= target <= nums[-1]:
            return binary_search(pivot, len(nums) - 1)
        
        return binary_search(0, pivot - 1)
