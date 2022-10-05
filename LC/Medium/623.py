# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(curr, curr_depth):
             if curr:
                if curr_depth == 1:
                    curr.left  = TreeNode(val, curr.left, None)
                    curr.right = TreeNode(val, None, curr.right)

                dfs(curr.left, curr_depth - 1)
                dfs(curr.right, curr_depth - 1)
        
        if depth == 1:
            return TreeNode(val, root, None)
        else:
            dfs(root, depth - 1)
            return root