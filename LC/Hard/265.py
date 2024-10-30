class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        cache = {}
        
        def dfs(i, prev):
            if i >= n:
                return 0
            if (i, prev) in cache:
                return cache[(i, prev)]
            
            res = inf
            
            for j in range(k):
                if j != prev:
                    res = min(res, dfs(i + 1, j) + costs[i][j])
            
            cache[(i, prev)] = res
            return res
        
        
        return dfs(0, -1)