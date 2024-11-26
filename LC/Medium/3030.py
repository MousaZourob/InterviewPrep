class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        ans = []
        intensity = defaultdict(list)
        
        def avg_reg(x, y):
            if x + 3 > m or y + 3 > n:
                return -1
            
            avg = 0
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if i + 1 < x + 3 and abs(image[i][j]-image[i+1][j]) > threshold:
                        return -1
                    if j + 1< y + 3 and abs(image[i][j]-image[i][j+1]) > threshold:
                        return -1
                    avg += image[i][j]
                        
            return avg//9   
        
        for r in range(m):
            ans.append(list(image[r]))
            for c in range(n):
                avg = avg_reg(r,c)
                if avg != -1:
                    for i in range(r, r+3):
                        for j in range(c, c+3):
                            intensity[(i,j)].append(avg)

        for i in range(m):
            for j in range(n):
                if intensity[(i,j)]:
                    ans[i][j] = sum(intensity[(i,j)])//len(intensity[(i,j)])
                    
        return ans
        