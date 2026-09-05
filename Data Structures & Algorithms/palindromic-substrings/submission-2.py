class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [1] * len(s)

        for i in range(0, len(s)):
            # even case
            l = r = i
            isEven = False
            if (i < len(s) - 1) and s[i] == s[i + 1]:
                dp[i] += 1 
                r += 1
                isEven = True
            while isEven and l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
                dp[i] += 1
                l -= 1
                r += 1
            
            # odd case
            l = r = i
            while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
                dp[i] += 1
                l -= 1
                r += 1
            if i > 0:
                dp[i] += dp[i - 1]

        print(dp)
        return dp[-1]