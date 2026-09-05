class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(i, j, k):
            nonlocal s1, s2, s3
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if i < len(s1) and j < len(s2) and dp[i][j] is not None:
                return dp[i][j]

            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    dp[i][j] = True
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    dp[i][j] = True
                    return True

            dp[i][j] = False
            return False
                
        dp = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        # print(dp)
        return dfs(0, 0, 0)
