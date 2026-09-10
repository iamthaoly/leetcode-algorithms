class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # input: string s, wordDict
        # output: True if s can be segmented into sequence of dictionary words
        # constraint: 
        # words in dictionary can be reused
        # all string in lowercase eng letters

        def dfs(s, i):
            if i > len(s):
                return len(s) == 0
            if (s, i) in dp:
                return dp[(s, i)]
                
            res = False
            if s[:i] in word_set:
                res = dfs(s[i:], 0)

            res = res or dfs(s, i + 1)
            dp[(s, i)] = res
            return res

        word_set = set(wordDict)
        dp = {}
        return dfs(s, 0)
            
