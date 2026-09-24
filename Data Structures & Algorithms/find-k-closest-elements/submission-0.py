class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = deque([])
        for num in arr:
            q.append([abs(num - x), num])
        # print(q)
        while len(q) > k:
            if q[0][0] > q[-1][0]:
                q.popleft()
            elif q[0][0] < q[-1][0]:
                q.pop()
            else:
                if q[0][1] > q[-1][1]:
                    q.popleft()
                else:
                    q.pop()
        res = [x[1] for x in q]
        return res


    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        # Min heap
        heap = []
        heapq.heapify(heap)
        for num in arr:
            heapq.heappush(heap, (-abs(num - x), num))
            # if len(heap) > k:
            #     heapq.heappop(heap)
        print(heap)
        # res = [x[1] for x in heap]
        # return res
