class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Solution 1: Bit manipulatin
        res = carry = 0

        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            sum_bit = bit_a ^ bit_b ^ carry
            carry = (bit_a + bit_b + carry) >= 2
            if sum_bit == 1:
                res = res | (1 << i)

        # To find the representation of -x:
        # 1. Write x
        # 2. Flip all bits
        # 3. Add 1
        
        # Handle negative numbers
        # mask is the largest positive 32-bit int
        # if res > mask -> negative res
        # res ^ mask: undoing the bit inversion part of two’s complement
        mask = 0xFFFFFFFF
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res
