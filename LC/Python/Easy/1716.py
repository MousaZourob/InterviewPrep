class Solution:
    def totalMoney(self, n: int) -> int:
        m = n // 7
        k = n % 7
        
        preWeek = m * 28 + 7 *((m - 1) * m // 2)
        lastWeek = k * (k + 1) // 2 + m * k
        
        return preWeek + lastWeek