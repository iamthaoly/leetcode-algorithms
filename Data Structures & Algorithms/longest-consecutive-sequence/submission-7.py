class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        end_nums = set()
        for num in set_nums:
            if num + 1 not in set_nums:
                end_nums.add(num)
        
        res = 0
        for num in end_nums:
            count = 0
            n = num
            while n in set_nums:
                count += 1
                n -= 1
            res = max(res, count)

        return res
