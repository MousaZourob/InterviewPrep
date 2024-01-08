# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(curr):
            if not curr:
                return 
            
            _sum = 0
            if low <= curr.val <= high:
                _sum += curr.val
            if curr.left:
                _sum += dfs(curr.left)
            if curr.right:
                _sum += dfs(curr.right)
            return _sum
        
        return dfs(root)