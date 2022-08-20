class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        intervals.sort(key = lambda i: i[0])
        ans = [intervals[0]]
        
        for interval in intervals[1:]:
            if ans[-1][1] >= interval[0]:
                ans[-1][1] = max(interval[1], ans[-1][1])
            else:
                ans.append(interval)
        
        return ans