class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Revision
        l = 0
        freq = {}
        max_char = s[0]
        res = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_char = s[r] if freq[s[r]] > freq[max_char] else max_char
            
            sub_len = r - l + 1
            if sub_len - freq[max_char] <= k:
                res = max(res, sub_len)
            else:
                freq[s[l]] -= 1
                l += 1
        return res
            
