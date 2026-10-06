class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Revise
        # Solution 1: Insert then merge
        intervals.append(newInterval)
        intervals.sort()

        cur = intervals[0]
        res = [cur]
        for i in intervals:
            if i[1] >= cur[0] and cur[1] >= i[0]:
                cur[1] = max(i[1], cur[1])
            else:
                res.append(i)
                cur = i

        return res
