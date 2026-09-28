class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = count = 0
        # for i in range(len(s)):
        #     if i > 0 and s[i] > s[i - 1]:
        #         count = roman[s[i]] - count
        #     else:
        #         res += count
        #         count = roman[s[i]]
        # res += count
        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                count += -roman[s[i]]
            else:
                count += roman[s[i]]
        # res += count
        return count