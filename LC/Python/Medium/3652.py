class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        half = k // 2
        total = sum(prices[i] * strategy[i] for i in range(n))
        
        prefix_strategy = [0] * (n + 1)
        prefix_prices = [0] * (n + 1)
        for i in range(n):
            prefix_strategy[i + 1] = prefix_strategy[i] + strategy[i] * prices[i]
            prefix_prices[i + 1] = prefix_prices[i] + prices[i]
        
        max_change = 0
        
        for i in range(n - k + 1):
            loss = prefix_strategy[i + half] - prefix_strategy[i]
            gain = (prefix_prices[i + k] - prefix_prices[i + half]) - (prefix_strategy[i + k] - prefix_strategy[i + half])
            net_change = gain - loss
            max_change = max(max_change, net_change)
        
        return total + max_change
