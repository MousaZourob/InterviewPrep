class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        ans = 0
        edges_used = 0
        
        heap = [(0, 0)]
        visited = [0] * n
        
        while edges_used < n:
            cost, source = heappop(heap)
            
            if visited[source]:
                continue
                
            visited[source] = True
            ans += cost
            edges_used += 1
            
            for i in range(n):
                if not visited[i]:
                    distance = (abs(points[source][0] - points[i][0]) +
                                abs(points[source][1] - points[i][1]))
                    heappush(heap, (distance, i))
                    
        return ans