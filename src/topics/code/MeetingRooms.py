
from typing import (
    List,
)

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        # Write your code here
        intervals.sort(key = lambda x:x.start)
        endi = intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start >= endi:
                endi = intervals[i].end
            else:
                return False
        return True




