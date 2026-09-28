class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj_list = [[] for _ in range(n)]
        degree = [0] * n 

        for u, v in edges:
            adj_list[u].append(v)
            degree[u] += 1
            adj_list[v].append(u)
            degree[v] += 1

        q = deque([])
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        # print(adj_list)
        remained = n
        while q and remained > 2:
            remained -= len(q)
            for _ in range(len(q)):
                i = q.popleft()
                for nb in adj_list[i]:
                    degree[nb] -= 1
                    if degree[nb] == 1:
                        q.append(nb)

        return list(q)
