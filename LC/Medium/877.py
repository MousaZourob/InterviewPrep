class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        
        def opt(l, r):
            if (l, r) in memo:
                return memo[(l,r)]
            if l > r: 
                return 0
            
            if (r - l + 1) % 2 == 0:
                memo[(l,r)] = max(piles[l] + opt(l + 1, r), piles[r] + opt(l, r - 1))
                return memo[(l,r)]
            else:
                memo[(l,r)] = min(-piles[l] + opt(l + 1, r), -piles[r] + opt(l, r - 1))
                return memo[(l,r)]
        
        return opt(0, len(piles)-1) > 0