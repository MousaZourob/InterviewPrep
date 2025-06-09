class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        
        for i in range(len(costs)):
            diff.append((costs[i][0] - costs[i][1], i))
        diff = sorted(diff, key=lambda a:a[0])
        cost = 0
        
        for i in range(len(diff)//2):
            cost += costs[diff[i][1]][0]
            
        for i in range(len(diff)//2, len(diff)):
            cost += costs[diff[i][1]][1]
            
        
        return cost