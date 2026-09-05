"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts = sorted(starts)
        ends = sorted(ends)
        n = len(intervals)

        l = r = 0
        room = 0
        while (l < n and r < n):
            if starts[l] < ends[r]:
                room += 1
                l += 1
            elif starts[l] >= ends[r]:
                l += 1
                r += 1
            
            # if l == n - 1 or r == n - 1:
            #     break

        return room
            
