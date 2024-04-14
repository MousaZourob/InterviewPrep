# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr, left):
            if not curr:
                return 0
            
            if left and not curr.right and not curr.left:
                return curr.val
            
            return dfs(curr.left, True) + dfs(curr.right, False)
                
        return dfs(root, False)