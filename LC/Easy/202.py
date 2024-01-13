class Solution:
    def isHappy(self, n: int) -> bool:
        def findSquare(n):
            squared = 0
            
            while n > 0:
                squared += (n % 10) ** 2
                n = n // 10
            
            return squared
            
        s, f = n, findSquare(n)
        
        while f != 1 and s != f:
            s = findSquare(s)
            f = findSquare(findSquare(f))
        
        return f == 1
        