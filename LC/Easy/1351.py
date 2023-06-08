class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid[0])
        index = n - 1
        
        for row in grid:
            while index >= 0 and row[index] < 0:
                index -= 1
            ans += (n - (index + 1))
        return ans