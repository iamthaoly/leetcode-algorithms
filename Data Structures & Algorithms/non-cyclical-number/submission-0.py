class Solution:
    def isHappy(self, n: int) -> bool:
        squares = set()
        while True:
            new_num = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                new_num += pow(digit, 2)
            if new_num == 1:
                return True
            if new_num in squares:
                return False
            squares.add(new_num)
            n = new_num

