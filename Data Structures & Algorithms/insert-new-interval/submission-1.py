class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Revise
        # Solution 2: Scan
        i, n = 0, len(intervals)
        res = []
        # 1. Add intervals that end before new interval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # 2. Merge overlapped intervals
        while i < n and intervals[i][1] >= newInterval[0] and newInterval[1] >= intervals[i][0]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        
        res.append(newInterval)

        # 3. Add intervals that end after new interval
        while i < n and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i += 1

        return res

        