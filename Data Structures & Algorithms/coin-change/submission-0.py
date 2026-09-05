class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        for c in coins:
            dp[c] = 1

        def solve(a):
            if a == 0:
                return 0
            if a in dp:
                return dp[a]

            min_r = float('inf')
            for coin in coins:
                if a - coin >= 0:
                    r = solve(a - coin)
                    if r != -1:
                        r += 1
                        min_r = min(min_r, r)
            dp[a] = -1 if min_r == float('inf') else min_r
            return dp[a]
        
        return solve(amount)
