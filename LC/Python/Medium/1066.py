class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        m = len(bikes)
        n = len(workers)
        
        queue = [(0, 0, 0)]
        visited = set()
        
        while True:
            distance, worker, taken = heappop(queue)
            
            if (worker, taken) in visited:
                continue
                
            visited.add((worker, taken))
            
            if worker == n:
                return distance
            
            for bike in range(m):
                if taken & (1 << bike) == 0:
                    bike_dist = (abs(workers[worker][0] - bikes[bike][0]) 
                                + abs(workers[worker][1] - bikes[bike][1]))
                    heappush(queue, (distance + bike_dist, worker + 1, taken | (1 << bike)))