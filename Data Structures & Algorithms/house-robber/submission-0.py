class Solution:
    def rob(self, nums: List[int]) -> int:
        m = [0] * (len(nums)+1)
        res = nums[0]
        # print(m)
        m[0] = nums[0]
        for i in range(1, len(nums)):
            m1 = m2 = 0
            if i - 2 >= 0:
                m1 = m[i - 2]
            if i - 3 >= 0:
                m2 = m[i - 3]

            m[i] = nums[i] + max(m1, m2)
            res = max(res, m[i])

        return res