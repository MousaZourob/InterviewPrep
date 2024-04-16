# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(curr):
            if not curr: return

            if curr.left and not curr.right:
                ans.append(curr.left.val)
            if curr.right and not curr.left:
                ans.append(curr.right.val)
            
            dfs(curr.left)
            dfs(curr.right)
        
        dfs(root)
        
        return ans