# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = [root]
        curr_depth = 0
        
        while q:
            n = len(q)
            curr_depth += 1
            
            for _ in range(n):
                curr = q.pop(0)
                if curr:
                    if not curr.right and not curr.left:
                        return curr_depth
                    
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
        
        return 0