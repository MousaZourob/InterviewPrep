class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if r * c != m * n:
            return mat
        
        ans = [[0] * c for _ in range(r)]
        
        x, y = 0, 0
        for i in range(m):
            for j in range(n):
                ans[x][y] = mat[i][j]
                y += 1
                if y == c:
                    x += 1
                    y = 0
        
        return ans