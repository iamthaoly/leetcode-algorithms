"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Revise
        # Solution 1: Sort + Min heap
        if len(intervals) <= 1:
            return len(intervals)

        heap = []
        intervals.sort(key = lambda x: x.start)
        res = 0
        for i in intervals:
            if not heap or i.start < heap[0][0]:
                pass
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, [i.end, i.start])
            res = max(res, len(heap))
        
        return res

