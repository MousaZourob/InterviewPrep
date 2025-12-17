class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            adj[u - 1].append(v - 1)

        def dfs(u):
            p_cost = present[u]
            d_cost = p_cost // 2
            p_profit = future[u] - p_cost
            d_profit = future[u] - d_cost

            sub_profit = [[0] * (budget + 1) for _ in range(2)]
            size = p_cost

            for v in adj[u]:
                child_res, child_size = dfs(v)
                size += child_size

                for state in range(2):
                    new_dp = [0] * (budget + 1)
                    for b in range(budget + 1):
                        if sub_profit[state][b] == 0 and b != 0:
                            continue
                        for cb in range(min(child_size, budget - b) + 1):
                            new_dp[b + cb] = max(
                                new_dp[b + cb],
                                sub_profit[state][b] + child_res[state][cb]
                            )
                    sub_profit[state] = new_dp

            res = [[0] * (budget + 1) for _ in range(2)]

            for b in range(budget + 1):
                res[0][b] = sub_profit[0][b]
                if b >= p_cost:
                    res[0][b] = max(
                        res[0][b],
                        sub_profit[1][b - p_cost] + p_profit
                    )

                res[1][b] = sub_profit[0][b]
                if b >= d_cost:
                    res[1][b] = max(
                        res[1][b],
                        sub_profit[1][b - d_cost] + d_profit
                    )

            return res, size

        return max(dfs(0)[0][0])
