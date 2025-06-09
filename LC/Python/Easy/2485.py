class Solution:
    def pivotInteger(self, n: int) -> int:
        l, r = 1, n
        
        total = n*(n+1) // 2
        
        while l <= r:
            m = (l + r) // 2
            pre_sum = m * (m+1) // 2
            post_sum = (n - m + 1) * (m+n) // 2

            if pre_sum == post_sum:
                return m
            elif pre_sum > post_sum:
                r = m - 1
            else:
                l = m + 1
        
        return -1
