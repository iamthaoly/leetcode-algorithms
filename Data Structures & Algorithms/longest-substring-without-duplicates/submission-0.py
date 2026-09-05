class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0

        while (l < len(s) and r < len(s)):
            while (r < len(s) - 1) and (not s[r+1] in s[l:r+1]):
                r += 1 
            max_len = max(max_len, r-l+1)
            l += 1
            r = max(r, l)
        
        return max_len
