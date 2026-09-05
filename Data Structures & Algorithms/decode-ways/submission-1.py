class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        dp["0"] = 0
        for i in range(1, 10):
            dp[str(i)] = 1
        for i in range(10, 27):
            dp[str(i)] = 2
        dp["10"] = dp["20"] = 1

        def solve(s, i):
            if i == len(s):
                return 0
            temp = s[i:]
            if temp[0] == "0":
                return 0
            if dp.get(temp):
                return dp[temp]

            res1 = res2 = 0
            s1 = s[i:i+1]
            n1 = int(s1)
            if 1 <= n1 <= 26:
                res1 = solve(s, i+1)
            
            s2 = s[i:i+2]
            n2 = int(s2)
            if 1 <= n2 <= 26:
                res2 = solve(s, i+2)

            dp[temp] = res1 + res2
            return dp[temp]
        
        res = solve(s, 0)
        return res
            