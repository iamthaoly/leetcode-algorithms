class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        # Fill 0
        for i in range(freq[0]):
            nums[i] = 0
        
        start = freq[0]
        for i in range(start, start + freq[1]):
            nums[i] = 1

        start += freq[1]
        for i in range(start, start + freq[2]):
            nums[i] = 2
