class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 1000

        l = 0
        r = len(nums) - 1

        while (l <= r):
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return res

