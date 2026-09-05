class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        p = prices
        dp = [[0 for _ in range(n)] for _ in range(n)]
        ans = 0
        # Bottom up
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                res = 0
                if p[j] - p[i] > 0:
                    res = p[j] - p[i] 
                    if j + 3 < n:
                        res += dp[j + 2][j + 3]
                # else:
                if j + 1 < n:
                    res = max(res, dp[i][j + 1], dp[i + 1][j + 1])
                dp[i][j] = res
                ans = max(ans, res)
        return ans

                

