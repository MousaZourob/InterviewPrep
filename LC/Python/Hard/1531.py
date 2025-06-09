class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = {}
        
        def dfs(i, k, prev, prev_count):  
            if k < 0:
                return inf
            if i == n:
                return 0
            if (i, k, prev, prev_count) in dp:
                return dp[(i, k, prev, prev_count)]
            
            if s[i] == prev:
                incr = 1 if prev_count in [1, 9, 99] else 0
                dp[(i, k, prev, prev_count)] = incr + dfs(i + 1, k, prev, prev_count + 1)
            else:
                dp[(i, k, prev, prev_count)] = min(dfs(i + 1, k - 1, prev, prev_count), 1 + dfs(i + 1, k, s[i], 1))
                
            return dp[(i, k, prev, prev_count)]
        
        return dfs(0, k, "", 0)