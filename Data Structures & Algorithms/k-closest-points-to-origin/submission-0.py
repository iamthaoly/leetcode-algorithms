class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        d = dict()
        for p in points:
            dist = round(math.sqrt(p[0]**2 + p[1]**2), 9)
            distances.append(dist)
            if not d.get(dist):
                d[dist] = [p]
            else:
                d[dist].append(p)

        heapq.heapify(distances)
        # print(d)

        res = []
        while k:
            p = heapq.heappop(distances)
            # res.append(d[p])
            res += list(d[p])
            d[p] = []
            k -= 1
        return res
