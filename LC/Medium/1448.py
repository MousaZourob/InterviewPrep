# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]
        
        def dfs(root, curr_max):
            if not root:
                return
            
            if curr_max <= root.val:
                ans[0] += 1
                curr_max = root.val
                
            dfs(root.left, curr_max)
            dfs(root.right, curr_max)
        
        dfs(root, root.val)
        
        return ans[0]