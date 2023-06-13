class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        
        for row in grid:
            rows[tuple(row)] += 1
                    
        ans = 0
        for c in range(len(grid)):
            col = [grid[i][c] for i in range(len(grid))]
            ans += rows[tuple(col)]
        
        return ans