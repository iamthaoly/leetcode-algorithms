class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        K = k
        adj_list = [[] for _ in range(n)]
        for u, v, p in flights:
            adj_list[u].append([v, p])

        cost = [[float('inf') for _ in range(k + 1)] for _ in range(n)]
        
        cost[src][0] = 0
        min_heap = [[0, 0, src]] # cost, k, node
        
        print(cost)
        while min_heap:
            cur_cost, k, cur = heapq.heappop(min_heap)
            if k > K:
                continue
            for nb, price in adj_list[cur]:
                new_cost = cur_cost + price
                if new_cost < cost[nb][k]:
                    cost[nb][k] = new_cost
                    heapq.heappush(min_heap, [new_cost, k + 1, nb])
                # if k + 1 <= K and new_cost < cost[nb]:
                #     cost[nb] = min(new_cost, cost[nb])
                #     heapq.heappush(min_heap, [cost[nb], k + 1, nb])
        
        # print(cost)
        res = min(cost[dst])
        return res if res != float('inf') else -1


