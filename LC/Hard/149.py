class Solution:
    def calculate_slope(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        
        if x1 == x2: return inf
        if y1 == y2: return 0
    
        return (y2 - y1) / (x2 - x1)
    
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        
        ans = 0
        
        for i in range(n):
            count = defaultdict(int)
            for j in range(i+1, n):
                slope = self.calculate_slope(points[i], points[j])
                count[slope] += 1
                ans = max(ans, count[slope])
                
        return ans + 1
    