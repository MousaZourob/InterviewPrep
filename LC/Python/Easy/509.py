class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        
        for _ in range(n):
            first, second = second, first + second
            
        return first