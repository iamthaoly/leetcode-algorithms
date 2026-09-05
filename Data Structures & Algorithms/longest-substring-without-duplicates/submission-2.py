class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        l = r = 0
        res = 0
        # Mistake 1:
        # Forget to extract char
        # Put l, r as dict key instead of s[l], s[r]

        while (r < len(s)):
            cr = s[r]
            chars[cr] = chars.get(cr, 0) + 1
            while chars[cr] > 1:
                cl = s[l]
                chars[cl] -= 1
                if chars[cl] == 0:
                    chars.pop(cl)
                l += 1
            res = max(res, r - l + 1)
            r += 1
        # print(chars)
        return res