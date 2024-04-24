class Solution:
    def tribonacci(self, n: int) -> int:        
        t1 = 0
        t2 = 1
        t3 = 1
        
        for _ in range(n):
            t3, t2, t1 = t3 + t2 + t1, t3, t2
        
        return t1