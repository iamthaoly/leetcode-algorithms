class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        p = prices
        dp = {}
        ans = 0
        
        # Bottom up - correct
        # Optimize memory

        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                res = 0
                if p[j] - p[i] > 0:
                    res = p[j] - p[i] 
                    if j + 3 < n:
                        res += dp.get((j + 2, j + 3), 0)
                if j + 1 < n:
                    # res = max(res, dp[i][j + 1], dp[i + 1][j + 1])
                    res = max(res, dp.get((i, j + 1), 0), dp.get((i + 1, j + 1), 0))
                dp[(i, j)] = res
                ans = max(ans, res)
        return ans

                

