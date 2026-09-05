class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        non_overlapping = 1
        prev = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[prev][1]:
                non_overlapping += 1
                prev = i

        return len(intervals) - non_overlapping
        