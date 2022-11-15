class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, 0
        
        for i in range(2, len(cost)+1):
            first, second = min(first + cost[i-1], second + cost[i-2]), first
        
        return first