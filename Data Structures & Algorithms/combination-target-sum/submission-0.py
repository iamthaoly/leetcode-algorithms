class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
        subsum = 0

        def dfs(i):
            nonlocal subsum
            if subsum >= target:
                if subsum == target:
                    res.append(subset.copy())
                return
            if i >= len(nums):
                # if subsum == target:
                #     res.append(subset.copy())
                return
            
            subset.append(nums[i])
            subsum += nums[i]
            dfs(i)
            # dfs(i + 1)
            
            if subset:
                val = subset.pop()
                subsum -= val
            dfs(i + 1)


        dfs(0)
        return res