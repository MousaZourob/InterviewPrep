class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        curr_dirr = "right"
        l, r = 0, n - 1
        t, b = 0, m - 1
        ans = []
        
        counter = 0
        while len(ans) < m*n:
            if curr_dirr == "right":
                for i in range(l, r+1):
                    ans.append(matrix[t][i])
                t += 1
                curr_dirr = "down"
                
            elif curr_dirr == "down":
                for i in range(t, b+1):
                    ans.append(matrix[i][r])
                r -= 1
                curr_dirr = "left"
            
            elif curr_dirr == "left":
                for i in range(r, l-1, -1):
                    ans.append(matrix[b][i])
                b -= 1
                curr_dirr = "up"
            
            elif curr_dirr == "up":
                for i in range(b, t-1, -1):
                    ans.append(matrix[i][l])
                l += 1
                curr_dirr = "right"
            
            counter += 1   
        
        return ans