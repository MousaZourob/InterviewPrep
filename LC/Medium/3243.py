class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        adj_list = [[i + 1] for i in range(n)]
        
        for s, e in queries:
            adj_list[s].append(e)
            
            q = deque([(0, 0)])
            visited = set()
            found = False
            while q:
                moves, curr = q.popleft()
                for neigh in adj_list[curr]:
                    if neigh == n - 1:
                        ans.append(moves + 1)
                        found = True
                        break
                    if neigh not in visited:
                        q.append((moves + 1, neigh))
                        visited.add(neigh)
                if found:
                    break
                    
        return ans