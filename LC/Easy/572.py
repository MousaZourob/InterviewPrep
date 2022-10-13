# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def search(curr):
            if not curr:
                return False
            
            if curr.val == subRoot.val:
                if dfs(curr, subRoot):
                    return True
               
            return search(curr.right) or search(curr.left)
        
        def dfs(p, q):
            if p and q:
                return p.val == q.val and dfs(p.left, q.left) and dfs(p.right, q.right)
            
            return p is q

        return search(root)