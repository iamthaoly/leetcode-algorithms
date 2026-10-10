class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Solution 2: DFS Reverse
        # Time: O(V * E)

        def dfs(source):
            while adj_list[source]:
                dest = adj_list[source].pop()
                dfs(dest)
            res.append(source)

        adj_list = defaultdict(list)
        for start, dest in tickets:
            adj_list[start].append(dest)
        for k in adj_list:
            adj_list[k].sort(reverse=True)

        res = []
        dfs("JFK")
        res.reverse()
        return res

