class Solution:
    def hammingWeight(self, n: int) -> int:
        # Solution 2: Hamming weight (Optimal)
        # Remove the rightmost 1 bit from n
        # Not waste time checking all bits

        # Subtract 1 from n: flips rightmost 1 to 0
        # And turns all bits on the right into 1
        # So n & (n - 1) -> Remove the rightmost 1
        
        count = 0
        while n > 0:
            count += 1
            n = n & (n - 1)
        return count
 
