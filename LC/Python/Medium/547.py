class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def dfs(curr):
            for nei, adj in enumerate(isConnected[curr]):
                if adj and nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        ans = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                ans += 1
        
        return ans