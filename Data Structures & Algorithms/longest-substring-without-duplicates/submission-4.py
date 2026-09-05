class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Revision
        # Solution 3: Sliding window + 1 dict (Optimal) 
        # Time: O(n) 
        # Space: O(m) 
        # n - len of s, m - total distinct char

        prev = {} # Prev position of char c
        l = r = 0
        res = 0

        # Mistake 1:
        # Forget to extract char
        # Put l, r as dict key instead of s[l], s[r]

        # Mistake 2
        # l = prev[s[l]] + 1 -> should be s[r]
        
        # Mistake 3
        # Not get max of (l, prev[s[r]] + 1)
        while (r < len(s)):
            if s[r] in prev:
                l = max(l, prev[s[r]] + 1)
            res = max(res, r - l + 1)
            prev[s[r]] = r
            r += 1
        print(prev)
        return res