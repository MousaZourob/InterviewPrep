class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        
        for i, eq in enumerate(equations):
            adj[eq[0]].append((eq[1], values[i]))
            adj[eq[1]].append((eq[0], 1 / values[i]))
        
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            
            q = [(src, 1)]
            visited = set()
            
            while q:
                curr, total = q.pop(0)
                
                if curr == target:
                    return total
                
                visited.add(curr)
                
                for neighbour, weight in adj[curr]:
                    if neighbour not in visited:
                        q.append((neighbour, total * weight))
            
            return -1
                
            
        
        return [bfs(q[0], q[1]) for q in queries]