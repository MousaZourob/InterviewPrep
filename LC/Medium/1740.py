# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def find_lca(curr):
            if not curr:
                return None
            
            if curr.val == p or curr.val == q:
                return curr
            
            left = find_lca(curr.left)
            right = find_lca(curr.right)
            
            if left and right:
                return curr
            
            return left if left else right
        
        def dfs(curr, target):
            if not curr:
                return -1

            res = -1
            if curr.val == target:
                return res + 1

            res = dfs(curr.left, target)
            if res >= 0:
                return res + 1
            
            res = dfs(curr.right, target)
            if res >= 0:
                return res + 1
            
            return res
        
        lca = find_lca(root)

        return dfs(lca, p) + dfs(lca, q)