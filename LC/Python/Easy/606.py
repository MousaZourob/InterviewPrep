# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        
        def dfs(curr):
            if not curr:
                return 
            
            ans.append(str(curr.val))
            
            if curr.left is None and curr.right is None:
                return
            
            ans.append('(')
            dfs(curr.left)
            ans.append(')')
            
            if curr.right:
                ans.append('(')
                dfs(curr.right)
                ans.append(')')
        
        dfs(root)

        return "".join(ans)