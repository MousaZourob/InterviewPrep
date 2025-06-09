# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = [root]
        
        while q:
            last_val = None
            
            for _ in range(len(q)):
                curr = q.pop(0)
                
                if curr:
                    last_val = curr.val
                
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            
            if last_val != None:
                ans.append(last_val)

        return ans