class Solution:
    def myPow(self, x: float, n: int) -> float:
        def divide(num, exp):
            if num == 0:
                return 0
            if exp == 0:
                return 1
            
            res = divide(num, exp // 2)
            res *= res
            
            return num * res if exp % 2 else res 
            
        ans = divide(x, n)
        if n >= 0:
            return ans
        else:
            return 1/ans