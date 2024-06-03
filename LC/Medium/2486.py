class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        ans = m
        t_i = 0
        
        for s_i in range(n):
            if t_i >= m:
                break
            if s[s_i] == t[t_i]:
                t_i += 1
                ans -= 1
        
        return ans