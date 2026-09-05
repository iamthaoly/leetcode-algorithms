class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Solution 1: Brute force + hash map
        if len(s1) > len(s2):
            return False
        freq1 = {}
        for c in s1:
            freq1[c] = freq1.get(c, 0) + 1

        k = len(s1)
        for i in range(len(s2) - k + 1):
            freq2 = {}
            cnt = 0
            for j in range(i, i + k):
                if s2[j] not in freq1:
                    break
                freq2[s2[j]] = freq2.get(s2[j], 0) + 1
                if freq2[s2[j]] > freq1[s2[j]]:
                    break
                if freq2[s2[j]] == freq1[s2[j]]:
                    cnt += 1
            if cnt == len(freq1):
                return True

        return False
            

