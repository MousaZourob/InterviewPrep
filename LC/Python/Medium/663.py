# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        seen = set()
        def dfs(curr):
            if not curr:
                return 0
            
            res = dfs(curr.left) + dfs(curr.right) + curr.val
            seen.add(res)
            return res

        total = dfs(root.left) + dfs(root.right) + root.val
        return total / 2 in seen
