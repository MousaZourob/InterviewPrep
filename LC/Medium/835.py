class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0
        
        def overlapping(r_offset, c_offset):
            count = 0
            
            for x in range(n):
                for y in range(n):
                    n_x = r_offset + x
                    n_y = c_offset + y
                    if 0 <= n_x < n and 0 <= n_y < n and img1[x][y] + img2[n_x][n_y] == 2:
                        count += 1
            return count
        
        for i in range(-n + 1, n):
            for j in range(-n + 1, n):
                ans = max(ans, overlapping(i, j))
        
        return ans