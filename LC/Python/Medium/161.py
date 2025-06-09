class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n = len(s) 
        m = len(t)
        
        if abs(n - m) > 1 or s == t:
            return False
        
        p1, p2 = 0, 0
        diff = 0
        
        while p1 < n and p2 < m:
            if s[p1] != t[p2]:
                diff += 1
                if diff > 1:
                    return False
                
                if n > m: 
                    p2 -= 1
                elif n < m:
                    p1 -= 1
            
            p1 += 1
            p2 += 1

                
        return True