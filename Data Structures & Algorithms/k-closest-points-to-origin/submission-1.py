class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Solution 3: Max heap
        # We want kth closest points (closest = smallest)
        # Use max heap
        d = [] 
        for x, y in points:
            d.append([-math.sqrt(x**2 + y**2), x, y])
        heapq.heapify(d)
        while len(d) > k:
            heapq.heappop(d)
        res = []
        for dist, x, y in d:
            res.append([x, y])

        return res