# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        def dfs(curr):
            if not curr:
                return None, None

            if curr.val <= target:
                left, right = dfs(curr.right)
                curr.right = left
                return curr, right
            else:
                left, right = dfs(curr.left)
                curr.left = right
                return left, curr
        
        return dfs(root)
