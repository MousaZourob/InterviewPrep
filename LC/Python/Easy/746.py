class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        jump_one = jump_two = 0
        
        for i in range(2, len(cost) + 1):
            jump_one, jump_two = min(jump_one + cost[i-1], jump_two + cost[i-2]), jump_one
        
        return jump_one