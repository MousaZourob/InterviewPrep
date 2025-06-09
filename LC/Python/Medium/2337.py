class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        l = 0
        r = 0
        
        for i in range(n):
            if start[i] == 'L':
                l -= 1
            elif start[i] == 'R':
                r += 1
                if l != 0: return False
            
            if target[i] == 'L':
                l += 1
                if r != 0: return False
            elif target[i] == 'R':
                r -= 1
                
            if l < 0 or r < 0: return False
        
        return l == 0 and r == 0
        