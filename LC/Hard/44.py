class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def remove_duplicates(p):
            new_string = []
            
            for c in p:
                if not new_string or c != '*':
                    new_string.append(c)
                elif new_string[-1] != '*':
                    new_string.append(c)
            
            return "".join(new_string)
        
        p = remove_duplicates(p)

        n = len(s)
        m = len(p)
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i,j)]
            if i == n and j == m:
                cache[(i,j)] = True
                return True
            if j == m:
                cache[(i,j)] = False
                return False
            if i == n:
                cache[(i,j)] = all(char == '*' for char in p[j:])
                return cache[(i,j)]
            
            res = False
            if s[i] == p[j] or p[j] == '?':
                res = dfs(i + 1, j + 1)
            elif p[j] == '*':
                res = dfs(i, j + 1) or dfs(i + 1, j)
            else:
                res = False
            
            cache[(i, j)] = res
            return res
                
        return dfs(0, 0)