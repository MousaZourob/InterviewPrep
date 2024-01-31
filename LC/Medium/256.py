class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        cache = {}
        
        def dfs(i, prev):
            if (i, prev) in cache:
                return cache[(i, prev)]
            if i >= n:
                return 0
            
            res = inf
            for j in range(3):
                if j != prev:
                    res = min(res, dfs(i+1, j) + costs[i][j])
            
            cache[(i, prev)] = res
            return res
            
        return dfs(0, -1)