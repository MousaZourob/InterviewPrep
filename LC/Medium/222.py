# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(curr):
            if not curr:
                return 0
            return 1 + dfs(curr.left)
        
        l, r = dfs(root.left), dfs(root.right)
        
        if l == r:
            return 2**l + self.countNodes(root.right)
        else:
            return 2**r + self.countNodes(root.left)