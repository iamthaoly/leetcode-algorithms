class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)
        
    def addNum(self, num: int) -> None:
        if not self.right or num >= self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        if len(self.right) - len(self.left) == 2:
            heapq.heappush(self.left, -heapq.heappop(self.right))
        elif len(self.left) - len(self.right) == 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        total = len(self.left) + len(self.right)
        if total == 0:
            return 0
        if total % 2 == 0:
            res = (-self.left[0] + self.right[0]) / 2
        else:
            res = self.right[0]

        return res
        