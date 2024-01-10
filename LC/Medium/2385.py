# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj_list = defaultdict(list)
        
        def dfs(curr):
            if not curr:
                return 
            
            if curr.left:
                adj_list[curr.val].append(curr.left.val)
                adj_list[curr.left.val].append(curr.val)
                dfs(curr.left)
            if curr.right:
                adj_list[curr.val].append(curr.right.val)
                adj_list[curr.right.val].append(curr.val)
                dfs(curr.right)
                
        dfs(root)
        
        q = [start]
        visited = set()
        visited.add(start)
        ans = 0
        
        while q:
            for _ in range(len(q)):
                curr = q.pop(0)
                
                for neighbour in adj_list[curr]:
                    if neighbour not in visited:
                        q.append(neighbour)
                        visited.add(neighbour)
            ans += 1
            
        
        return ans-1
            