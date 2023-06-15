# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDistance = [inf]
        prevNode = [None]
        
        def inorder(curr):
            if not curr: return
            
            inorder(curr.left)
            if prevNode[0]:
                minDistance[0] = min(minDistance[0], curr.val - prevNode[0].val)
            prevNode[0] = curr
            inorder(curr.right)
        
        inorder(root)
        return minDistance[0]