class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort()
        last_end = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start >= last_end:
                last_end = end
            else:
                ans += 1
                last_end = min(end, last_end)
        
        return ans