class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Revision 
        # Bottom up
        if sum(nums) % 2 != 0:
            return False
        if len(nums) == 1:
            return False

        target = sum(nums) // 2
        dp = {}
        # 1. Fill col 0 (target = 0)
        # No number can achieve target 0
        for i in range(len(nums)):
            dp[(i, 0)] = False
        
        for t in range(target + 1):
            dp[(0, t)] = (nums[0] == t)
        
        for i in range(1, len(nums)):
            for t in range(1, target + 1):
                skip = dp[(i - 1, t)]
                remain = t - nums[i]
                include = False
                if remain >= 0:
                    include = dp[(i - 1, remain)]
                dp[(i, t)] = skip or include
                    
        return dp[(len(nums) - 1, target)]
        