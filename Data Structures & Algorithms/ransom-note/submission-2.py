class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_chars = defaultdict(int)
        magazine_chars = defaultdict(int)

        for ch in magazine:
            magazine_chars[ch] += 1
        for ch in ransomNote:
            ransom_chars[ch] += 1

        for ch in ransom_chars:
            if ch not in magazine_chars or magazine_chars[ch] < ransom_chars[ch]:
                return False

        return True
