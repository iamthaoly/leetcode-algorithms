class Solution:
    def hammingWeight(self, n: int) -> int:
        # Solution 1: most obvious
        # Check if n has at least 1 bit set, until n > 0
        # Then shift n to right
        count = 0
        while n > 0:
            count += (n & 1)
            n = n >> 1
        return count
