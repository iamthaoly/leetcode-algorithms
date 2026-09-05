class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        #res = [-1, -1]
        # resLen = infinity
        chars_need_to_match = len(countT) # the number of unique chars in t to match
        chars_matched = 0

        freq = dict()
        l = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            if (s[r] in countT) and (freq[s[r]] == countT[s[r]]):
                chars_matched += 1
            
            while chars_matched == chars_need_to_match:
                if r-l+1 < len(res) or res == "":
                    res = s[l:r+1]
                freq[s[l]] -= 1
                if (s[l] in countT) and (freq[s[l]] < countT[s[l]]):
                    chars_matched -= 1
                l += 1
        return res




