# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        balanced = [True]
        
        def dfs(curr):
            if not balanced[0]:
                return False
            
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            if abs(left - right) > 1:
                balanced[0] = False
            
            return max(left, right) + 1
        
        dfs(root)
        return balanced[0]