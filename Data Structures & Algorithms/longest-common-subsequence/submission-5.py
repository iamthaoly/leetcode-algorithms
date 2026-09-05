class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a, b = text1, text2
        dp = [[None for _ in b] for _ in a]
        
        def solve(i, j):
            if i >= len(a) or j >= len(b):
                return 0
            if dp[i][j]:
                return dp[i][j]
            
            if a[i] == b[j]:
                res = 1 + solve(i + 1, j + 1)
            else:
                res = max(solve(i + 1, j), solve(i, j + 1))

            dp[i][j] = res
            return res

        return solve(0, 0)