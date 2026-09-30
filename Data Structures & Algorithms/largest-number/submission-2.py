from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            return 1

        if max(nums) == 0:
            return "0"

        arr = [str(num) for num in nums]
        # arr.sort(key=cmp_to_key(compare))
        arr = sorted(arr, key=cmp_to_key(compare))
        res = "".join(arr)

        return res

        