class Solution:
    def longestPalindrome(self, s: str) -> int:
        # input: s
        # output: longest palindrome to build
        # pattern: count char, 
        
        # approach: freq[i] - freq[i]%2
        # remove from the dict if freq = 0
        # if the dict is empty, count + 1

        # mistakes:
        # remove item from the dict
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
        
        palindrome = 0
        chars_left = 0
        for char in freq:
            count = freq[char] if freq[char] % 2 == 0 else freq[char] - 1
            freq[char] -= count
            if freq[char] > 0:
                chars_left += 1

            palindrome += count

        if chars_left > 0:
            palindrome += 1
        
        return palindrome

 