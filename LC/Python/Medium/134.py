class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        ans = 0
        tank = 0
        for i, station in enumerate(zip(gas, cost)):
            tank += station[0] - station[1]
            
            if tank < 0:
                tank = 0
                ans = i + 1
            
        return ans