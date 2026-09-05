class Solution:
    def canJump(self, nums: List[int]) -> bool:        
        # Greedy approach
        # Track leftmost
        left_most = len(nums) - 1
        i = len(nums) - 2
        
        while(i >= 0):
            if nums[i] + i >= left_most:
                left_most = i
            i -= 1
        
        return left_most == 0
        