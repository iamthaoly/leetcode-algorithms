class Solution:
    def countBits(self, n: int) -> List[int]:
        # Solution 2 - dynamic programming
        # Time: O(n)
        dp = [0] * (n + 1)
        dp[0] = 0
        offset = 0
        for i in range(1, n + 1):
            if i > 0 and (i & (i - 1) == 0):
                offset = i

            dp[i] = 1 + dp[i - offset]

        return dp
        

        


