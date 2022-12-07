# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = [0]
        
        def dfs(curr):
            if not curr: 
                return
            
            if curr.val <= high and curr.val >= low: 
                ans[0] += curr.val      
            if curr.val < high:
                dfs(curr.right)
            if curr.val > low:
                dfs(curr.left)
        
        dfs(root)
        return ans[0]