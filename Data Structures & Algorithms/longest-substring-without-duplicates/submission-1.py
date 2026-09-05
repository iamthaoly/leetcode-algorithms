class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l = 0
        # r = 0
        # max_len = 0

        # while (l < len(s) and r < len(s)):
            
        #     while (r < len(s) - 1) and (not s[r+1] in s[l:r+1]):
        #         r += 1 
        #     max_len = max(max_len, r-l+1)
        #     l += 1
        #     r = max(r, l)
        
        # return max_len

        l = 0
        r = 0
        max_len = 0
        chars = set()

        # NEXT: CODE NEW SOLUTION USING SET
        while (l < len(s) and r < len(s)):
            chars.add(s[l])
            while (r < len(s) - 1) and (not s[r + 1] in chars):
                r += 1
                chars.add(s[r])

            max_len = max(max_len, r-l+1)
            if (s[l] in chars):
                chars.remove(s[l])
            l += 1
            r = max(l, r)
        return max_len
