class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = dict[int, bool]()  # dictionary with number as key
 
        for num in nums:
            if num in check:
                return True
            check[num] = True
      
        return False