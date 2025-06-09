# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = [None]
        
        def dfs(curr):
            if not curr:
                return False

            left = dfs(curr.left)
            right  = dfs(curr.right)

            mid = curr == p or curr == q

            if left + right + mid >= 2:
                ans[0] = curr

            return left or right or mid
                
        dfs(root)
        return ans[0]