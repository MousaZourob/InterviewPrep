# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            return TreeNode(val, root)
                
        def dfs(curr, curr_depth):
            if not curr: return
            
            if curr_depth + 1 == depth:
                curr.left = TreeNode(val, curr.left)
                curr.right = TreeNode(val, None, curr.right)
                return
            
            dfs(curr.left, curr_depth + 1)
            dfs(curr.right, curr_depth + 1)
    
        dfs(root, 1)
        
        return root