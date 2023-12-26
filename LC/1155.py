class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        
        def dfs(i, total):
            if i > n:
                return 0
            if i == n:
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = 0
            for j in range(1, k + 1):
                dp[(i, total)] += dfs(i + 1, total + j)
            
            return dp[(i, total)]
        
        return dfs(0, 0) % (10**9 + 7)