class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        bipartition = {}
        
        for node in range(len(graph)):
            if node in bipartition:
                continue
            q = [node]
            bipartition[node] = 1
            
            while q:
                curr = q.pop()
                
                for neighbour in graph[curr]:
                    if neighbour in bipartition:
                        if bipartition[curr] == bipartition[neighbour]:
                            return False
                    else:
                        bipartition[neighbour] = bipartition[curr] * -1
                        q.append(neighbour)

        return True