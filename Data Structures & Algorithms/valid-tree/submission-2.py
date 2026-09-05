class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        a = [[] for _ in range(n)]
        for edge in edges:
            a[edge[0]].append(edge[1])
            a[edge[1]].append(edge[0])

        visited = set()

        def dfs(i, parent):
            if i in visited:
                return False
            visited.add(i)

            if a[i] == []:
                return True
            
            for v in a[i]:
                if parent == v:
                    continue
                if not dfs(v, i):
                    return False

            a[i] = []
            return True
            
        return dfs(0, None) and len(visited) == n

