class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = []
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = "#"
        
        for r, c in q:
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + x
                nc = c + y
                
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == "#":
                    mat[nr][nc] = 1 + mat[r][c]
                    q.append((nr, nc))
                    
        return mat