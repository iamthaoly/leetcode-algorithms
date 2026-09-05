class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def solve(s, i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if dp.get(i):
                return dp[i]

            res = solve(s, i+1)
            
            if i+1 < len(s):
                n2 = int(s[i:i+2])
                if 10 <= n2 <= 26:
                    res += solve(s, i+2)

            dp[i] = res
            return dp[i]
        
        res = solve(s, 0)
        return res
            