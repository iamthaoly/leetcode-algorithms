class Solution:
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Top Down
        def dfs(i, remain):
            if i == len(nums):
                return remain == 0
            if i > len(nums):
                return 0
            if (i, remain) in dp:
                return dp[(i, remain)]

            dp[(i, remain)] = dfs(i + 1, remain - nums[i]) + dfs(i + 1, remain + nums[i])
            return dp[(i, remain)]
        
        dp = {}
        return dfs(0, target)


    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        def dfs(i, remain):
            if i == len(nums):
                return remain == 0
            if i > len(nums):
                return 0

            count = dfs(i + 1, remain - nums[i]) + dfs(i + 1, remain + nums[i])
            return count
        
        return dfs(0, target)


