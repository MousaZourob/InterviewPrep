# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        
        def dfs(curr):
            if not curr:
                return True
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            if left and right:
                if curr.left and curr.left.val != curr.val:
                    return False
                if curr.right and curr.right.val != curr.val:
                    return False
                
                ans[0] += 1
                return True
            else:
                return False
        
        
        dfs(root)
        
        return ans[0]