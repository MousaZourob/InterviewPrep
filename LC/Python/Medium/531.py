class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        ans = 0
        n = len(picture)
        m = len(picture[0])
        
        row_count = [0] * n
        col_count = [0] * m
        
        for row in range(n):
            for col in range(m):
                if picture[row][col] == 'B':
                    row_count[row] += 1
                    col_count[col] += 1
        
        for row in range(n):
            for col in range(m):
                if picture[row][col] == 'B' and row_count[row] == 1 and col_count[col] == 1:
                    ans += 1
        
        return ans