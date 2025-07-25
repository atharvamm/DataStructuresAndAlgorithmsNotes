

from typing import (
    List,
)

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        # Write your code here
        import heapq
        end_times = []
        min_ends = heapq.heapify(end_times)
        intervals.sort(key = lambda x:x.start)
        print([[ele.start,ele.end] for ele in intervals])
        min_rooms = 1
        heapq.heappush(end_times, intervals[0].end)
        for i in range(1,len(intervals)):
            if intervals[i].start >= end_times[0]:
                heapq.heappop(end_times)
            heapq.heappush(end_times, intervals[i].end)
            min_rooms = max(min_rooms, len(end_times))
        return min_rooms