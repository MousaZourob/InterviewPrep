class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        cache = {}
        
        def dfs(n, k):
            if k == 0:
                return 1
            if n == 1 or k < 0:
                return 0
            if (n, k) in cache:
                return cache[(n, k)]
            
            res = 0
            
            res = (dfs(n - 1, k) + dfs(n, k - 1) - dfs(n - 1, k - n)) % (10**9 + 7)
                
            cache[(n, k)] = res
            
            return res
        
        return dfs(n, k)