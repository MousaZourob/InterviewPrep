class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {}
        
        def opt(i, diff):
            if i == len(rods):
                return 0 if diff == 0 else -inf
            if (i, diff) in dp:
                return dp[(i, diff)]
            
            left = rods[i] + opt(i+1, diff + rods[i])
            right = opt(i+1, diff - rods[i])
            none = opt(i+1, diff)
            
            dp[(i, diff)] = max(left, right, none)
            return dp[(i, diff)]
        
        return opt(0, 0)