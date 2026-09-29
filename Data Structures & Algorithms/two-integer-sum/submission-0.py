class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1: Dict, Set
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        
        for i in range(len(nums)):
            remained = target - nums[i]
            if remained in nums_dict and nums_dict[remained] != i:
                return sorted([i, nums_dict[remained]])
                