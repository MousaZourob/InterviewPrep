class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1
        
        for _ in range(n):
            first, second = second, first + second
            
        return first