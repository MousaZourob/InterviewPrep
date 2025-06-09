class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = {}
        
        def opt(i, buy):
            if i >= n:
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            
            ans = opt(i + 1, buy)
            if buy:
                ans = max(ans, opt(i+1, False) - prices[i])
            else:
                ans = max(ans, opt(i+1, True) + prices[i] - fee)
            dp[(i, buy)] = ans
            return ans
        
        return opt(0, True)