class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            source, dest = edges[i]
            cost = succProb[i]
            graph[source].append((dest, cost))
            graph[dest].append((source, cost))
        
        max_prob = [0.0] * n 
        max_prob[start_node] = 1.0
        
        q = [(-1.0, start_node)]
        while q:
            curr_prob, curr_node = heappop(q)
            
            if curr_node == end_node:
                return -curr_prob
            
            for neigh, neigh_prob in graph[curr_node]:
                if neigh_prob * -curr_prob > max_prob[neigh]:
                    max_prob[neigh] = neigh_prob * -curr_prob
                    heappush(q, (-max_prob[neigh], neigh))
        
        return 0.0
        