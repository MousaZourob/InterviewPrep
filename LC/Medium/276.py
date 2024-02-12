class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        
        two_back = k
        one_back = k*k
        
        for i in range(2, n):
            one_back, two_back = (k - 1) * (one_back + two_back), one_back

        return one_back