class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        adjacency_list = defaultdict(list)
        visited = {}
        
        for a, b, dist in highways:
            adjacency_list[a].append((b, dist))
            adjacency_list[b].append((a, dist))

        q = [(0, 0, discounts)]
        while q:
            curr_cost, curr_node, curr_disc = heappop(q)
            
            if curr_node in visited and curr_disc <= visited[curr_node]: 
                continue
		    
            visited[curr_node] = curr_disc

            if curr_node == n - 1:
                return curr_cost
            
            for neigh, neigh_cost in adjacency_list[curr_node]:
                if curr_disc > 0:
                    heappush(q, (curr_cost + neigh_cost // 2, neigh, curr_disc - 1))
                heappush(q, (curr_cost + neigh_cost, neigh, curr_disc))
     
        return -1