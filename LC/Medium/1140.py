class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        n = len(piles)
        
        def opt(i, m, turn):
            if (i, m, turn) in memo:
                return memo[(i, m, turn)]
            if i == n: 
                return 0
            
            res = -1 if turn == 0 else inf  
            
            total = 0
            for x in range(1, min(2*m, n-i) + 1):
                total += piles[i+x-1]
                if turn == 0:
                    res = max(res, total + opt(i + x, max(m, x), 1))
                else:
                    res = min(res, opt(i + x, max(m, x), 0))
                    
            memo[(i, m, turn)] = res
            return res
        
        return opt(0, 1, 0)