class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        ans = [0]*cols
        
        
        for col in range(cols):
            curr_col = col
            for row in range(rows):
                next_col = curr_col + grid[row][curr_col]
                if next_col < 0 or next_col > cols-1 or grid[row][curr_col] != grid[row][next_col]:
                    ans[col] = -1
                    break
                ans[col] = next_col
                curr_col = next_col
                
        return ans
            