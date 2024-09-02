class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        s_reverse = s[::-1]
        cache = {}
        
        def dfs(i, j):
            if i == n or j == n:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == s_reverse[j]:
                cache[(i, j)] = 1 + dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            
            return cache[(i, j)]
        
        return n - dfs(0, 0)
