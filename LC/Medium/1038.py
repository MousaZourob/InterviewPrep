# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        prev_sum = [0]
        def dfs(curr):
            if not curr: return
            
            dfs(curr.right)
            prev_sum[0] += curr.val
            curr.val = prev_sum[0]
            dfs(curr.left)
        
        dfs(root)
        return root
