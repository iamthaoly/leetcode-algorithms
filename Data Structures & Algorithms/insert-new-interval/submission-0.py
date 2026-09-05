class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        res = []
        nt = newInterval
        j = 0
        i = intervals[j]

        while j < len(intervals) and nt[0] > i[1]:
            res.append(i)
            j += 1
            if j >= len(intervals):
                break
            i = intervals[j]

        while j < len(intervals) and nt[0] <= i[1] and nt[1] >= i[0]:
            nt[0] = min(nt[0], i[0])
            nt[1] = max(nt[1], i[1])
            j += 1
            if j >= len(intervals):
                break
            i = intervals[j]

        res.append(nt)

        while j < len(intervals):
            res.append(i)
            j += 1
            if j >= len(intervals):
                break
            i = intervals[j]

        return res

