class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        def helper(i, j):
            submatrix = [grid[i][j], grid[i][j+1], grid[i+1][j], grid[i+1][j+1]]
            count = {'B': 0, 'W': 0}
            
            for c in submatrix:
                count[c] += 1
            
            return count['B'] >= 3 or count['W'] >= 3 
        
        
        return (helper(0,0) or helper(0, 1) or helper(1, 0) or helper(1,1))