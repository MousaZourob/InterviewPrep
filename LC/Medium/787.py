class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        
        for source, dest, cost in flights:
            adj_list[source].append((dest, cost))

        queue = [(0, src, 0)]
        steps = [float(inf)] * n
                
        while queue:
            cost, source, flights_taken = heappop(queue)
            
            if flights_taken > steps[source] or flights_taken > k + 1:
                continue
                
            steps[source] = flights_taken
                
            if source == dst:
                return cost
                            
            for neighbour, travel_cost in adj_list[source]:
                heappush(queue, (cost + travel_cost, neighbour, flights_taken + 1))

        return -1