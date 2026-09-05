class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        
        def solve(amount, i):
            if i > len(coins) - 1:
                return 0
            if amount == 0:
                return 1
            if dp.get((amount, i)):
                return dp[(amount, i)]
            
            r1 = solve(amount, i + 1)
            r2 = 0
            if amount >= coins[i]:
                r2 = solve(amount - coins[i], i)
            # else:
            #     r2 = solve(amount, i + 1)
            
            dp[(amount, i)] = r1 + r2
            return r1 + r2
            
        return solve(amount, 0)
