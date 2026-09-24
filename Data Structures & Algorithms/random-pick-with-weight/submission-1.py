class Solution:

    def __init__(self, w: List[int]):
        # self.w = w
        sum_w = sum(w)
        arr = [0] * sum_w

        j = 0
        # num_j = w[0]
        for i in range(sum_w):
            while w[j] == 0:
                j += 1
                # num_j = w[j]

            arr[i] = j
            w[j] -= 1

        self.arr = arr
        

    def pickIndex(self) -> int:
        i = random.randint(0, len(self.arr) - 1)
        return self.arr[i]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()