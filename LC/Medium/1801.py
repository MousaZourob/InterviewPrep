class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_orders = []
        sell_orders = []
        
        for price, amount, t in orders:
            if t == 0:
                heappush(buy_orders, [-price, amount])
            else:
                heappush(sell_orders, [price, amount])
            
            while buy_orders and sell_orders and sell_orders[0][0] <= -buy_orders[0][0]:
                quantity = min(buy_orders[0][1], sell_orders[0][1])
                buy_orders[0][1] -= quantity
                sell_orders[0][1] -= quantity
                if buy_orders[0][1] == 0:
                    heappop(buy_orders)
                if sell_orders[0][1] == 0:
                    heappop(sell_orders)
                    
        return sum(amount for price, amount in buy_orders + sell_orders) % (10**9 + 7)