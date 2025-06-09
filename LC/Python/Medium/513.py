# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = [-1]
        ans = [0]
        
        def dfs(curr, curr_depth):
            if not curr:
                return
            
            if curr_depth > max_depth[0]:
                max_depth[0] = curr_depth
                ans[0] = curr.val

            dfs(curr.left, curr_depth + 1)
            dfs(curr.right, curr_depth + 1)
        
        dfs(root, 0)
        return ans[0]