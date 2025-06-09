class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[start[0]][start[1]] = True
        q = [[start[0], start[1]]]
        
        while q:
            r, c = q.pop(0)
            
            if r == destination[0] and c == destination[1]:
                return True
            
            for x,y in [[0,1], [1,0], [0,-1], [-1,0]]:
                nr, nc = r, c
                while 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == 0:
                    nr += x
                    nc += y
                
                nr -= x
                nc -= y
                
                if not visited[nr][nc]:
                    q.append([nr,nc])
                    visited[nr][nc] = True

        return False