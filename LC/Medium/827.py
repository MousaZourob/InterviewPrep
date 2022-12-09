# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        level1 = []
        level2 = []
        
        def dfs(curr, lvl):
            if not curr:
                return
            
            if not curr.right and not curr.left:
                lvl.append(curr.val)
                return
            else:
                dfs(curr.left, lvl)
                dfs(curr.right, lvl)
        
        dfs(root1, level1)
        dfs(root2, level2)

        return level1 == level2