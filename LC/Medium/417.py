class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: 
            return []
        
        m = len(heights)
        n = len(heights[0])
        pac_reachable = set()
        atl_reachable = set()
        
        def dfs(row, col, reachable):
            reachable.add((row, col))
            
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row, new_col = row + x, col + y
                
                if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                    continue

                if (new_row, new_col) in reachable:
                    continue

                if heights[new_row][new_col] < heights[row][col]:
                    continue

                dfs(new_row, new_col, reachable)
        
        for i in range(m):
            dfs(i, 0, pac_reachable)
            dfs(i, n - 1, atl_reachable)
        for i in range(n):
            dfs(0, i, pac_reachable)
            dfs(m - 1, i, atl_reachable)
        
        return list(pac_reachable.intersection(atl_reachable))