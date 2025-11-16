class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        
        cons_ones = 0
        for c in s:
            if c == '1':
                cons_ones += 1
                ans += cons_ones
            else:
                cons_ones = 0

        return ans % (10**9 + 7)
