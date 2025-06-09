class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)
        ans = 1
        
        while l <= r:
            m = (l + r) // 2
            used_stores = 0
            for q in quantities:
                used_stores += ceil(q/m)
            
            if used_stores <= n:
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans