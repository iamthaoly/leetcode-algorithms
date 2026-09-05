class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
        subsum = 0

        # optimal solution
        nums = sorted(nums)
        def dfs(i):
            nonlocal subsum
            if subsum == target:
                res.append(subset.copy())
                return
            if subsum > target or i >= len(nums):
                return

            subset.append(nums[i])
            subsum += nums[i]
            dfs(i)

            temp = subsum
            val = subset.pop()
            subsum -= val
            if temp > target:
                return
            dfs(i + 1)
        
        dfs(0)
        return res