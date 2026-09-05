class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Solution 2: Sliding window + char array (optimal)
        # Time: O(n)
        # Space: O(1) (26 chars)
        if len(s1) > len(s2):
            return False

        f1 = [0] * 26
        f2 = [0] * 26
        match_cnt = 0
        k = len(s1)
        a = ord('a')

        for i in range(k):
            f1[ord(s1[i]) - a] += 1
            f2[ord(s2[i]) - a] += 1
        
        for i in range(26):
            if f2[i] == f1[i]:
                match_cnt += 1
        
        l = 0
        for r in range(k, len(s2)):
            if match_cnt == 26:
                return True

            cr = ord(s2[r]) - ord('a')
            f2[cr] += 1
            if f2[cr] == f1[cr]:
                match_cnt += 1
            elif f2[cr] - 1 == f1[cr]:
                match_cnt -= 1
            
            cl = ord(s2[l]) - ord('a')
            f2[cl] -= 1
            if f2[cl] == f1[cl]:
                match_cnt += 1
            elif f2[cl] + 1 == f1[cl]:
                match_cnt -= 1
            
            l += 1

        return match_cnt == 26


