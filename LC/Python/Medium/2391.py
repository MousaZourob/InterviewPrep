class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        count = 0
        truck_travel = defaultdict(int)
        travel_time = 0
        travel.append(0)
        
        for i, g in enumerate(garbage):
            count += len(g)
            for t in g:
                truck_travel[t] = travel_time
            travel_time += travel[i]
        
        return count + sum(truck_travel.values())
        