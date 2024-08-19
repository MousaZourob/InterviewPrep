class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        cache = {}
        def dfs(curr_len, paste_len):
            if (curr_len, paste_len) in cache:
                return cache[curr_len, paste_len]
            
            if curr_len == n:
                return 0
            
            if curr_len > n:
                return inf
            
            res = min(2 + dfs(curr_len*2, curr_len), 1 + dfs(curr_len + paste_len, paste_len))
            cache[(curr_len, paste_len)] = res
            
            return res
            
        return 1 + dfs(1, 1)