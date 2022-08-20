class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key = lambda i: i.start)
        
        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False

        return True