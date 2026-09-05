class Solution:
    def reverseBits(self, n: int) -> int:
        k = 31
        res = 0
        while(n > 0):
            if (n & 1) == 1:
                res = res | (1 << k)
            n = n >> 1
            k -= 1

        return res
