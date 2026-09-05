class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # tracked = set()

        a = sorted(nums)
        for i in range(0, len(a)-2):
            temp = a[i]
            if temp > 0: 
                break
            if i > 0 and a[i] == a[i - 1]:
                continue
            l = i + 1
            r = len(a) - 1
            while l < r:
                three_sum = temp + a[l] + a[r]
                if three_sum > 0:
                    r -= 1
                if three_sum < 0:
                    l += 1
                if three_sum == 0:
                    res += [[temp, a[l], a[r]]]
                    r -= 1
                    l += 1
                    while l < r and a[l] == a[l - 1]:
                        l += 1

        
        return res
