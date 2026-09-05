class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
        # print(dp)

        # Tips: 
        # When convert Top Down -> Bottom up
        # Change dp[][] default value from None to 0 or equivalent

        for i in range(0, amount + 1):
            for j in range(len(coins)-1, -1, -1):
                if i == 0:
                    dp[i][j] = 1
                    continue
                if amount - coins[j] >= 0:
                    r1 = dp[i][j + 1] if j + 1 <= len(coins) else 0
                    r2 = dp[i - coins[j]][j] 
                    dp[i][j] = r1 + r2

        return dp[amount][0]