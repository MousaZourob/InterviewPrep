class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a1 = (ay2 - ay1) * (ax2 - ax1)
        a2 = (by2 - by1) * (bx2 - bx1)
        
        ans = a1+a2        
        
        ox = min(ax2, bx2) - max(ax1, bx1)
        oy = min(ay2, by2) - max(ay1, by1)
            
        if ox > 0 and oy > 0:
            oa = ox*oy
        else:
            oa = 0
        
        return ans - oa 