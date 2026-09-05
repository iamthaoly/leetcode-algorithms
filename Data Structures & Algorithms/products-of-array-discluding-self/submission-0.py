class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input: int arr nums
        # output: product of all items in nums except nums[i]
        # constraint:
        # - each product fit 32-bit int
        # - num[i] can be negative, 0
        # - len(nums) >= 2
        # prod = 1
        # for num in nums:
        #     prod *= num
        
        # res = []
        # for i in range(len(nums)):
        #     res.append(product / nums[i])
        
        # get prefix product, suffix product of nums[i]
        prefix = [None] * len(nums)
        suffix = [None] * len(nums)
        prefix[0] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        suffix[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # prefix = [1, 1, 2, 8]
        # suffix = [48, 24, 6, 1]
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res








