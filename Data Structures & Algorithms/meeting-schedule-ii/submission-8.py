"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Solution 2: Greedy
        # Find max number of meetings happening at the same time
        
        max_cur_meeting = cur_meeting = 0
        time = []
        for i in intervals:
            time.append([i.start, 1])
            time.append([i.end, -1])

        time.sort(key = lambda x: (x[0], x[1]))
        for i in time:
            cur_meeting += i[1]
            max_cur_meeting = max(max_cur_meeting, cur_meeting)

        return max_cur_meeting


