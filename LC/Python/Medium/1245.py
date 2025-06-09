class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        
        for parent, child in edges:
            adj_list[parent].append(child)
            adj_list[child].append(parent)
            
        ans = [0]
        
        def dfs(curr, parent):
            max1, max2 = 0, 0
            
            res = 0
            
            for neighbour in adj_list[curr]:
                if neighbour == parent:
                    continue
                
                res = 1 + dfs(neighbour, curr)
                    
                if res > max1:
                    max2 = max1
                    max1 = res
                elif res > max2:
                    max2 = res
            
            ans[0] = max(ans[0], max1 + max2)
            
            return max1
                
        dfs(0, -1)
        
        return ans[0]