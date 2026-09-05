class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Input: nums = [1,2,3]
        # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        res = []
        subset = []
 
        def backtrack(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # exclude nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res

