class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        
        for source, dest, cost in times:
            adj_list[source].append((dest, cost))
            
        ans = 0
        visited = {}
        heap = [(0, k)]
        
        while heap:
            cost, source = heappop(heap)
            
            if source in visited:
                continue
                
            visited[source] = True
            ans = max(ans, cost)
            
            for neighbour, n_cost in adj_list[source]:
                if neighbour not in visited:
                    heappush(heap, (n_cost + ans, neighbour))
        
        return ans if len(visited) == n else -1