class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        cache = {}

        # state: 0 = flat, 1 = long, 2 = short
        # transactions = completed transactions so far
        def dfs(i, transactions, state):
            if (i, transactions, state) in cache:
                return cache[(i, transactions, state)]
            if transactions == k:
                return 0 if state == 0 else float("-inf")
            if i == n:
                return 0 if state == 0 else float("-inf")

            p = prices[i]
            if state == 0:
                res = max(
                    dfs(i + 1, transactions, 0),
                    dfs(i + 1, transactions, 1) - p,
                    dfs(i + 1, transactions, 2) + p
                )
            elif state == 1:
                res = max(
                    dfs(i + 1, transactions, 1),
                    dfs(i + 1, transactions + 1, 0) + p
                )
            else:
                res = max(
                    dfs(i + 1, transactions, 2),
                    dfs(i + 1, transactions + 1, 0) - p
                )

            cache[(i, transactions, state)] = res
            return res

        return dfs(0, 0, 0)
