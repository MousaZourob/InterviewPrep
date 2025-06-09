# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:    
        def dfs(curr):
            if not curr:
                return None
            
            curr.left = dfs(curr.left)
            curr.right = dfs(curr.right)
            
            if curr.left is curr.right and curr.val == target:
                return None
            
            return curr
            
        return dfs(root)