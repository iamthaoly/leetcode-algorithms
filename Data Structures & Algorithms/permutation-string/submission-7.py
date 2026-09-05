class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = [0] * 26
        f2 = [0] * 26
        match_cnt = 0
        k = len(s1)
        a = ord('a')

        for c in s1:
            f1[ord(c) - a] += 1
        
        l = 0
        for c in s2[:k]:
            f2[ord(c) - a] += 1
        
        for i in range(len(f2)):
            if f2[i] == f1[i]:
                match_cnt += 1
        
        l = 0
        for r in range(k, len(s2)):
            if match_cnt == 26:
                return True

            cr = ord(s2[r]) - ord('a')
            if f2[cr] == f1[cr]:
                match_cnt -= 1
            f2[cr] += 1
            if f2[cr] == f1[cr]:
                match_cnt += 1
            
            cl = ord(s2[l]) - ord('a')
            if f2[cl] == f1[cl]:
                match_cnt -= 1
            f2[cl] -= 1
            if f2[cl] == f1[cl]:
                match_cnt += 1
            
            l += 1

        return match_cnt == 26


