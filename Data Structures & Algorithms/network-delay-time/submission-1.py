class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)] # 1 - n
        for u, v, t in times:
            graph[u].append([v, t])

        distances = [float('inf')] * (n + 1)
        distances[k] = 0

        min_heap = [[0, k]]
        visited = set()

        while min_heap:
            dist, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            for v, weight in graph[u]:
                new_dist = dist + weight
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    if v not in visited:
                        heapq.heappush(min_heap, [new_dist, v])
        
        res = max(distances[1:])

        return -1 if res == float('inf') else res

