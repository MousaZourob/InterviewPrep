class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        n = len(grid)
        dirr = [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        q = [(0,0)]
        visited = {(0,0)}
        ans = 1
        
        def get_neighbours(x,y):
            for x_off, y_off in dirr:
                new_x = x + x_off
                new_y = y + y_off
                
                if 0 <= new_x < n and 0 <= new_y < n and not grid[new_x][new_y] and (new_x, new_y) not in visited :
                    yield (new_x, new_y)
        
        while q:
            length = len(q)
            
            for _ in range(length):
                r,c = q.pop(0)
                
                if r == n-1 and c == n-1:
                    return ans
                
                for neigh in get_neighbours(r,c):
                    q.append(neigh)
                    visited.add(neigh)
            
            ans += 1
        
        return -1
        