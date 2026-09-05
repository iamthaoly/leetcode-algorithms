class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a, b = text1, text2
        dp = [[None for _ in b] for _ in a]
        
        for i in range(len(a)-1, -1, -1):
            for j in range(len(b)-1, -1, -1):
                if a[i] == b[j]:
                    dp[i][j] = 1 
                    if i < len(a)-1 and j < len(b)-1:
                        dp[i][j] += dp[i + 1][j + 1]
                else:
                    res = 0
                    if j < len(b) - 1:
                        res = dp[i][j + 1]
                    if i < len(a) - 1:
                        res = max(res, dp[i + 1][j])
                    
                    dp[i][j] = res

        return dp[0][0]

