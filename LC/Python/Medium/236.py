# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        def dfs(curr):
            if not curr or curr == p or curr == q:
                return curr
            
            l = dfs(curr.left)
            r = dfs(curr.right)
            
            if l and r:
                return curr
            
            return l or r
            
        
        return dfs(root)