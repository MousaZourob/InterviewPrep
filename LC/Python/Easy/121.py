class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = 0
        ans = 0
    
        for i in range(1, len(prices)):
            if (prices[curr_min] > prices[i]):
                curr_min = i
            ans = max(ans, prices[i] - prices[curr_min])    
        
        
        return ans