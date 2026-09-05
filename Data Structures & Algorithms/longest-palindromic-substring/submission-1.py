class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        

        for i in range(0, len(s)):
            l = r = i
            # even case
            isEven = False
            if i + 1 < len(s) and s[i] == s[i + 1]:
                r += 1
                isEven = True
            while isEven and l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            res = s[l:r+1] if r - l + 1 > len(res) else res

            l = r = i
            while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            
            res = s[l:r+1] if r - l + 1 > len(res) else res

        return res