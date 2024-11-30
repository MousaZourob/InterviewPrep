class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        neigh = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(moveTime)
        n = len(moveTime[0])
        
        q = [(0, 0, 0)]
        visited = set()
        
        while q:
            time, r, c = heappop(q)
            
            if r == m - 1 and c == n -1:
                return time
            
            if (r, c) in visited:
                continue
            visited.add((r, c))
            
            for x, y in neigh:
                nr = r + x
                nc = c + y
                
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    time_to_visit = max(time + 1, moveTime[nr][nc] + 1)
                    heappush(q, (time_to_visit, nr, nc))
                    
        return -1