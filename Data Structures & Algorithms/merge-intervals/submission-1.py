class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()

        res = []
        cur = intervals[0]
        res.append(cur)
        for i in range(1, len(intervals)):
            it = intervals[i]
            if cur[0] <= it[1] and it[0] <= cur[1]:
                # cur = [min(cur[0], it[0]), max(cur[1], it[1])]
                cur[1] = max(cur[1], it[1])
            else:
                cur = it
                res.append(cur)

        return res



