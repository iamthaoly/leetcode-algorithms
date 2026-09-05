class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        p = prices
        dp = [[None for _ in range(n)] for _ in range(n)]

        def solve(i, j):
            if i >= n or j >= n:
                return 0
            if dp[i][j]:
                return dp[i][j]
            
            res = 0
            if p[j] - p[i] > 0:
                res = p[j] - p[i] + solve(j + 2, j + 3)
            
            res = max(res, solve(i, j + 1), solve(i + 1, j + 1))
            
            dp[i][j] = res
            return res
        
        return solve(0, 1)