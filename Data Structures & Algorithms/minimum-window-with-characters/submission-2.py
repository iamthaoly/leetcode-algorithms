class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freqT = defaultdict(int)
        freqS = defaultdict(int)
        for ch in t:
            freqT[ch] += 1
        
        l = r = count = 0
        min_len = float('inf')
        res = [-1, -1]
        for r in range(len(s)):
            freqS[s[r]] += 1
            if s[r] in freqT and freqS[s[r]] == freqT[s[r]]:
                count += 1

            while l <= r and count == len(freqT):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = [l, r]
                # shink L
                if s[l] in freqT and freqS[s[l]] == freqT[s[l]]:
                    count -= 1
                freqS[s[l]] -= 1
                l += 1

        return s[res[0]:res[1]+1] if min_len != float('inf') else ""

            

