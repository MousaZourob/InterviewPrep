class Solution:
    def myPow(self, x: float, n: int) -> float:
        def divide(num, exp):
            if exp == 1:
                return num
            if exp == 0:
                return 1
            if num == 0:
                return 0
            
            res = divide(num, exp // 2)
            res *= res
            
            return num * res if exp % 2 else res 
            
        ans = divide(x, abs(n))
        if n >= 0:
            return ans
        else:
            return 1/ans