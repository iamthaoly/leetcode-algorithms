class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution 2: Boyer Moore voting algo
        cnt = 0
        candidate = None
        for num in nums:
            if cnt == 0:
                candidate = num
            if num == candidate:
                cnt += 1
            else:
                cnt -= 1

        return candidate

    def majorityElement2(self, nums: List[int]) -> int:
        # Solution 1: Dictionary
        # O(n) space
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
            if freq[num] > len(nums) // 2:
                return num
        
