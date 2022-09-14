# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        paths = []
        ans = [0]
        
        def dfs(curr, pairs):
            if not curr:
                return 0
            
            if curr.val in pairs:
                pairs.remove(curr.val)
            else:
                pairs.add(curr.val) 

            if not curr.right and not curr.left:
                return 1 if len(pairs) <= 1 else 0

            l_count = dfs(curr.left, set(pairs))
            r_count = dfs(curr.right, set(pairs))

            return l_count + r_count
        
        return dfs(root, set())