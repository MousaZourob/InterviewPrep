class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for parent, child in connections:
            adj_list[parent].append((child, 1))
            adj_list[child].append((parent, 0))
            
        ans = 0    
        q = deque()
        q.append(0)
        visited = [0 for _ in range(n)]
        visited[0] = 1
        
        while q:
            curr = q.pop()

            for neighbour, dirr in adj_list[curr]:
                if not visited[neighbour]:
                    visited[neighbour] = 1
                    q.append(neighbour)
                    ans += dirr
                
        return ans