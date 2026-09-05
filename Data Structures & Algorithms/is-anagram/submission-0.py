class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1, f2 = dict(), dict()

        for c in s:
            f1[c] = f1.get(c, 0) + 1
        for c in t:
            f2[c] = f2.get(c, 0) + 1

        if len(f1) != len(f2):
            return False
        
        for char in f1:
            if f1.get(char) != f2.get(char):
                return False

        return True