class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        
        cache = {}
        def dfs(l, r, removals):
            if l >= r:
                return True
            if s[l] != s[r] and removals == 0:
                return False
            if (l, r, removals) in cache:
                return cache[(l, r, removals)]
            
            res = False

            if s[l] == s[r]:
                res = dfs(l + 1, r - 1, removals) 
            else:
                res = dfs(l + 1, r, removals - 1) or dfs(l, r - 1, removals - 1)
            
            cache[(l, r, removals)] = res
            
            return res
        
        
        return dfs(0, n-1, k)