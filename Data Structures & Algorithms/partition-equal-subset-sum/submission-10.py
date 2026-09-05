class Solution:
    def canPartition(self, nums: [int]) -> bool:
        # Revision 
        # Bottom up (Space optimized)
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
        # dp[0] = True  # Can make sum 0 by choosing nothing
        dp[nums[0]] = True
        # 1. Fill col 0 (target = 0)
        # No number can achieve target 0
        # for i in range(len(nums)):
        #     dp[(i, 0)] = False
        
        # 2. Fill row 0 (nums[0] vs target)
        # for t in range(target + 1):
        #     dp[t] = (nums[0] == t)
        
        # 3. Process from (1, 1)
        # Make t go backwards so
        # dp[t - nums[i]] still represent the previous row.
        for i in range(1, len(nums)):
            for t in range(target, -1, -1):
                skip = dp[t]
                remain = t - nums[i]
                include = False
                if remain >= 0:
                    include = dp[remain]
                dp[t] = skip or include
                    
        return dp[target]

    def canPartition2(self, nums: List[int]) -> bool:
        # Revision 
        # Bottom up
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        dp = {}
        # 1. Fill col 0 (target = 0)
        # No number can achieve target 0
        for i in range(len(nums)):
            dp[(i, 0)] = False
        
        # 2. Fill row 0 (nums[0] vs target)
        for t in range(target + 1):
            dp[(0, t)] = (nums[0] == t)
        
        # 3. Process from (1, 1)
        for i in range(1, len(nums)):
            for t in range(1, target + 1):
                skip = dp[(i - 1, t)]
                remain = t - nums[i]
                include = False
                if remain >= 0:
                    include = dp[(i - 1, remain)]
                dp[(i, t)] = skip or include
                    
        return dp[(len(nums) - 1, target)]


        