class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        for child, parent in adjacentPairs:
            adj[parent].append(child)
            adj[child].append(parent)
            
        root = None
        for num in adj:
            if len(adj[num]) == 1:
                root = num
                break
        
        curr = root
        ans = [root]
        prev = None
        
        while len(ans) < len(adj):
            for n in adj[curr]:
                if n != prev:
                    ans.append(n)
                    prev = curr
                    curr = n
                    break
        return ans
            