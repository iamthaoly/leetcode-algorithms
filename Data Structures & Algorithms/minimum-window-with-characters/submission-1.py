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
        res = ""
        for r in range(len(s)):
            freqS[s[r]] += 1
            if s[r] in freqT and freqS[s[r]] == freqT[s[r]]:
                count += 1

            while l <= r and count == len(freqT):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r+1]
                # shink L
                if s[l] in freqT and freqS[s[l]] == freqT[s[l]]:
                    count -= 1
                freqS[s[l]] -= 1
                l += 1

        return res

    # def minWindow2(self, s: str, t: str) -> str:
    #     if len(t) > len(s):
    #         return ""
    #     freqT = defaultdict(int)
    #     freqS = defaultdict(int)
    #     for ch in t:
    #         freqT[ch] += 1

    #     l = r = count = 0
    #     min_len = float('inf')

    #     for r in range(len(s)):
    #         freqS[s[r]] += 1
    #         if s[r] in freqT and freqS[s[r]] == freqT[s[r]]:
    #             count += 1
    #         if count == len(freqT):
    #             min_len = r - l + 1
    #             break



    #     return min_len
    #     while r < len(s):
    #         if count == len(freqT):
    #             min_len = min(min_len, r - l + 1)

    #         if s[r] not in freqT:
    #             r += 1
    #             continue

    #         while r < len(s) and count < len(freqT):
    #             if freqS[s[r]] == freqT[s[r]]:
    #                 count -= 1
    #             r += 1
    #             freqS[s[r]] += 1
    #             if freqS[s[r]] == freqT[s[r]]:
    #                 count += 1
            
    #         if count == len(freqT):
    #             min_len = min(min_len, r - l + 1)
            

