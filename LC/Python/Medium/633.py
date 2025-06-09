class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))
        while a <= b:
            curr = a * a + b * b
            
            if curr == c: 
                return True
            
            if curr < c:
                a += 1
            else:
                b -= 1

        return False
