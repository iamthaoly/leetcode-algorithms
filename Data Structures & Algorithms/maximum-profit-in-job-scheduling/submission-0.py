class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def dfs(i, j):
            if j == len(startTime):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = dfs(i, j + 1)
            if i is None or intervals[i][0] >= intervals[j][1] or intervals[j][0] >= intervals[i][1]:
                res = max(res, intervals[j][2] + dfs(j, j + 1))
            
            dp[(i, j)] = res
            return res

        
        intervals = []
        for i in range(len(startTime)):
            intervals.append([startTime[i], endTime[i], profit[i]])
        
        intervals.sort(key=lambda x: (x[1], x[0]))
        # intervals.sort()
        # print(intervals)
        dp = {}
        return dfs(None, 0)
