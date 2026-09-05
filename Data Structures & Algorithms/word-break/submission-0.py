class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        # cant use set
        dp = {}
        # n = len(s)
        def solve(s):
            if s == "":
                return True
            if s in dp:
                return dp[s]
            if s in wordDict:
                dp[s] = True
                return True

            for w in wordDict:
                i = s.find(w)
                if i != -1:
                    l = s[0:i]
                    r = s[i+len(w):]
                    res = solve(l) and solve(r)
                    if res:
                        dp[s] = True
                        return True
            dp[s] = False
            return False

        res = solve(s)
        # print(dp)
        return res
            
