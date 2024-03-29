# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even = True
        
        q = [root]
        
        while q:
            prev = -inf if even else inf

            for _ in range(len(q)):
                curr = q.pop(0)
                
                if even:
                    if prev >= curr.val or curr.val % 2 == 0:
                        return False
                else: 
                    if prev <= curr.val or curr.val % 2 == 1:
                        return False
                
                prev = curr.val
                
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
            even = not even
        
        return True