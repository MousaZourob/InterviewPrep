class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = l
        
        while l <= r:
            m = (l+r) // 2
            time = 0
            for b in piles:
                time += ceil(b/m)
            if time <= h:
                r = m - 1
                ans = m
            else:
                l = m + 1
        
        return ans