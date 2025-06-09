class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}
        cuts = [0] + sorted(cuts) + [n]
        
        def opt(left, right):
            if (left, right) in dp:
                return dp[(left,right)]
            if right - left == 1:
                return 0
            dp[(left,right)] = min(opt(left, mid) + opt(mid, right) + cuts[right] - cuts[left] for mid in range(left + 1, right))
            return dp[(left, right)]
            
        return opt(0, len(cuts) - 1)