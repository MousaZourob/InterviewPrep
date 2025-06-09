class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = -inf
        held = -inf
        reset = 0
        
        for price in prices:
            sold, held, reset = held + price, max(held, reset - price), max(reset, sold)
            
        return max(sold, reset)