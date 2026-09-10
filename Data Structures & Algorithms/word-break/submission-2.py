class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # PRACTICE
        # Time: O(n³) 
        # Space: O(n²)
        # String slicing costs O(n)
        # Optimize by only passing i and compare to the wordset in dfs

        # input: string s, wordDict
        # output: True if s can be segmented into sequence of dictionary words
        # constraint: 
        # words in dictionary can be reused
        # all string in lowercase eng letters

        # def dfs(s, i):
        #     if i > len(s):
        #         return len(s) == 0
        #     if (s, i) in dp:
        #         return dp[(s, i)]
                
        #     res = False
        #     if s[:i] in word_set:
        #         res = dfs(s[i:], 0)

        #     res = res or dfs(s, i + 1)
        #     dp[(s, i)] = res
        #     return res
        def dfs(i): # Optimized
            # Base case
            if i in dp:
                return dp[i]
            if i >= len(s):
                return True
                
            for j in range(i, min(len(s), i + limit)):
                if s[i : j + 1] in word_set:
                    if dfs(j + 1):
                        dp[i] = True
                        return True
            dp[i] = False
            return False

        word_set = set(wordDict)
        dp = {}
        # Optimize 2: Set iteration limit
        limit = len(max(wordDict, key=len))
        return dfs(0)
            
