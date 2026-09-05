class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(numCourses)]
        # courses = {}
        # for p in prerequisites:
        #     if not courses.get(p[0]):
        #         courses[p[0]] = [] 
        #     courses[p[0]].append(p[1])
        for p in prerequisites:
            courses[p[0]].append(p[1])

        print(courses)
        
        def dfs(i):
            if i in path:
                return False
            if len(courses[i]) == 0:
                return True

            path.add(i)
            for nb in courses[i]:
                if not dfs(nb):
                    return False

            path.remove(i)
            courses[i] = []
            return True
        
        for c in range(numCourses):
            path = set()
            if not dfs(c):
                return False
        
        return True
            

        
        