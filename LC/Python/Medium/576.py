class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        cache = {}
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        
        def dfs(r, c, currMoves):
            if (r, c, currMoves) in cache:
                return cache[(r, c, currMoves)]
            if r == m or c == n or r < 0 or c < 0:
                return 1
            if currMoves == maxMove:
                return 0
            
            cache[(r, c, currMoves)] = 0
            for x, y in dirs:
                cache[(r, c, currMoves)] += dfs (r + x, c + y, currMoves+1)
            
            return cache[(r, c, currMoves)]
        
        return dfs(startRow, startColumn, 0) % (10**9 + 7)