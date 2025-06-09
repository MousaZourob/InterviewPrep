# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:     
        def dfs(curr, value):
            if not curr:
                return 0
            
            value *= 10
            value += curr.val
            
            if not curr.left and not curr.right:
                return value
                        
            return dfs(curr.left, value) + dfs(curr.right, value)
        
        
        return dfs(root, 0)