class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = dict()
        max_freq = 0
        l = 0

        for r in range(0, len(s)):
            freq[s[r]] = (freq.get(s[r], 0)) + 1
            max_freq = max(freq[s[r]], max_freq)          

            while (l <= r):
                window_size = r - l + 1
                replace_need = window_size - max_freq
                if replace_need > k:
                    freq[s[l]] -= 1
                    l += 1
                else:
                    res = max(res, window_size)
                    break

        return res


            
