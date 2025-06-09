class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [False] * n
        ans = []
        
        for edge in edges:
            incoming[edge[1]] = True
        
        for i, node in enumerate(incoming):
            if not node:
                ans.append(i)
                
        return ans
        