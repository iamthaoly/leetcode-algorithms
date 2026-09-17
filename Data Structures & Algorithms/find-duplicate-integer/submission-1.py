class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        slow = fast = 0
        slow2 = None

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                slow2 = 0
                break

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
