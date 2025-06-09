class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = inf
        min2 = inf
        
        for price in prices:
            if price < min1:
                min2 = min1
                min1 = price
            else:
                min2 = min(min2, price)
               
        ans = money - min1 - min2
        return ans if ans >= 0 else money