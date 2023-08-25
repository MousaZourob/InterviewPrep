class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = {}
        
        def dfs(n, m):
            if (n, m) in dp:
                return dp[(n, m)] == 1
            if n + m == len(s3):
                return True
            
            res = False 
            if n < len(s1) and s1[n] == s3[n + m]:
                res |= dfs(n + 1, m)
            
            if m < len(s2) and s2[m] == s3[n + m]:
                res |= dfs(n, m + 1)
            
            dp[(n, m)] = 1 if res else 0
            return res
            
        
        return dfs(0, 0)
        