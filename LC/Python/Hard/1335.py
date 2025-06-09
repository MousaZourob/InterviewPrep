class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        
        if n < d:
            return -1 
        
        dp = {}
        
        def dfs(i, remaining, cur_max):
            if i >= n:
                return 0 if remaining == 0 else inf
            if remaining == 0:
                return inf
            if (i, remaining, cur_max) in dp:
                return dp[(i, remaining, cur_max)]
            
            cur_max = max(cur_max, jobDifficulty[i])
            
            dp[(i, remaining, cur_max)] = min(
                dfs(i + 1, remaining, cur_max),
                cur_max + dfs(i + 1, remaining - 1, 0)
            )
            
            return dp[(i, remaining, cur_max)]
        
        
        return dfs(0, d, 0)