"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        start_pointer, end_pointer = 0,0
        used_rooms = 0
        max_rooms = 0

        while start_pointer < len(intervals):

            if starts[start_pointer] < ends[end_pointer]:
                used_rooms += 1
                start_pointer += 1

            else:
                used_rooms -= 1
                end_pointer += 1

            
            max_rooms = max(max_rooms,used_rooms)

        return max_rooms
