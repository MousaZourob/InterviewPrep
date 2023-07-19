class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adj = defaultdict(list)

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        q = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        safe = [False] * n
        while q:
            node = q.pop(0)
            safe[node] = True
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        safeNodes = []
        for i in range(n):
            if safe[i]:
                safeNodes.append(i)

        return safeNodes