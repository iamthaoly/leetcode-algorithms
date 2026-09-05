class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        a = [[] for _ in range(n)]
        for u, v in edges:
            a[u].append(v)
            a[v].append(u)

        visited = set()

        def dfs(i, parent):
            if i in visited:
                return

            visited.add(i)
            for v in a[i]:
                if v == parent:
                    continue
                dfs(v, i)
            
            a[i] = []

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i, None)
        return count
