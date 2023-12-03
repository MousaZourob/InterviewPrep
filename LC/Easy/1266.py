class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        
        for i in range(1, len(points)):
            start = points[i-1]
            target = points[i]
            time += max(abs(target[0] - start[0]), abs(target[1] - start[1]))
            
        return time