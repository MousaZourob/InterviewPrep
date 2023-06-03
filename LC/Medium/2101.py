class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        
        
        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            for j in range(i + 1, len(bombs)):
                x2, y2, r2 = bombs[j]
                d = sqrt((x1 - x2)**2 + (y1-y2)**2)
                
                if d <= r1:
                    adj_list[i].append(j)
                if d <= r2:
                    adj_list[j].append(i)
                    
        def dfs(i, visited):
            if i in visited:
                return 0
            
            visited.add(i)
            for neigh in adj_list[i]:
                dfs(neigh, visited)
            
            return len(visited)
        
        ans = 0
        
        for i in range(len(bombs)):
            ans = max(ans, dfs(i, set()))
        
        return ans