class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        m = len(bikes)
        worker_bike_dist = []
        queue = []
        
        for worker, worker_pos in enumerate(workers):
            curr_pairs = []
            for bike, bike_pos in enumerate(bikes):
                distance = abs(worker_pos[0] - bike_pos[0]) + abs(worker_pos[1] - bike_pos[1])
                curr_pairs.append((distance, worker, bike))
            
            curr_pairs.sort(reverse = True)
            heappush(queue, curr_pairs.pop())
            worker_bike_dist.append(curr_pairs)
            
        bike_chosen = [False] * m
        worker_bike_picks = [-1] * n
        
        while queue:
            distance, worker, bike = heappop(queue)
            
            if not bike_chosen[bike]:
                worker_bike_picks[worker] = bike
                bike_chosen[bike] = True
            else:
                next_closest_bike = worker_bike_dist[worker].pop()
                heappush(queue, next_closest_bike)
        
        return worker_bike_picks