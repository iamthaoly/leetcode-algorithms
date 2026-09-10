class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Mistakes
        # - Append list ref to res instead of a copy

        def backtrack(num):
            # if num in visited:
            #     return

            cur.append(num)
            visited.add(num)

            if len(cur) == len(nums):
                res.append(cur.copy())

            for n in nums:
                if n not in visited:
                    backtrack(n)

            cur.pop()
            visited.remove(num)
        
        res, cur = [], []
        visited = set()
        for n in nums:
            backtrack(n) 
        return res