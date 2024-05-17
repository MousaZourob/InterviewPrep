# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr.left and not curr.right:
                return curr.val
            
            if curr.val == 2:
                return dfs(curr.left) or dfs(curr.right)
            else:
                return dfs(curr.left) and dfs(curr.right)
        
        return dfs(root)