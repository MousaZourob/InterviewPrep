class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph =  [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        q = [source]
        visited = set()
        
        while q:
            curr = q.pop()
            if curr == destination:
                return True
            
            visited.add(curr)
            
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    q.append(neighbour)
        
        return False