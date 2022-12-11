class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i,buy)]
            
            skip = dfs(i+1, buy) 
            if buy:
                bought = dfs(i+1, not buy) - prices[i]
                dp[(i, buy)] = max(skip, bought)
            else:
                sold = dfs(i+2, not buy) + prices[i]
                dp[(i, buy)] = max(skip, sold)
            return dp[(i, buy)]
        
        return dfs(0, True)