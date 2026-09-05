class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        # The second time identify wrong base case for bottom up
        
        # Identify leaf node
        # In top down, root is (0, 0)
        # -> Leaf is: (-1, -1)
        dp[-1][-1] = True # Can form empty string 
        # print(dp[len(s1)][len(s2)])
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = dp[i + 1][j]
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = dp[i][j + 1]
                
        return dp[0][0]





