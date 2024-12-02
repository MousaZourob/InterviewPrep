class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        for house in range(n - 2, -1, -1):
            costs[house][0] += min(costs[house+1][1], costs[house+1][2])
            costs[house][1] += min(costs[house+1][0], costs[house+1][2])
            costs[house][2] += min(costs[house+1][0], costs[house+1][1])
        
        return min(costs[0])