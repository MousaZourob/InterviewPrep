class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        cache = {}
        
        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if m - i < n - j:
                return 0
            
            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            
            cache[(i, j)] = res
            
            return res
            
        
        return dfs(0 ,0)