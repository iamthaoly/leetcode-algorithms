class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological sort
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for u, v in prerequisites:
            adj_list[v].append(u)
            indegree[u] += 1

        q = deque([u for u in range(numCourses) if indegree[u] == 0])
        topo_order = []
        while q:
            u = q.popleft()
            topo_order.append(u)
            for v in adj_list[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return topo_order if len(topo_order) == numCourses else []



        
        


