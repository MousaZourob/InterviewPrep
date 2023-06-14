class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = defaultdict(int)
        n = len(prob)
        
        def op(i, heads):
            if (i, heads) in dp:
                return dp[(i, heads)]
            
            if heads < 0:
                return 0
            
            if i == n and heads == 0:
                return 1
            
            if i >= n:
                return 0
            
            dp[(i, heads)] = op(i + 1, heads - 1) * prob[i] + op(i + 1, heads) * (1 - prob[i])
            
            return dp[(i, heads)]
        
        return op(0, target)