class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda b: b[1])
        
        ans = 0
        curr_arrow = None
        
        for start, end in points:
            if not curr_arrow or start > curr_arrow:
                ans += 1
                curr_arrow = end
        
        return ans