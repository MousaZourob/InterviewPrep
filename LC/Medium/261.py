class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not  n:
            return True
        
        adj_list = defaultdict(list)
        
        for parent, child in edges:
            adj_list[parent].append(child)
            adj_list[child].append(parent)
            
        visited = set()
        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            for i in adj_list[curr]:
                if i == prev:
                    continue
                
                if not dfs(i, curr):
                    return False
            
            return True
        
        
        return dfs(0, -1) and n == len(visited)