class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        ans = []
        
        def dfs(curr, path):
            for neigh in graph[curr]:
                path.append(neigh)
                if neigh == target:
                    ans.append(list(path))
                else:
                    dfs(neigh, path)
                path.pop()
            
        dfs(0, [0])
        return ans