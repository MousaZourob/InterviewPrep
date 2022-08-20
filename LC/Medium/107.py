# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = [root]
        
        while q:
            curr_level = []
            
            for i in range(len(q)):
                curr = q.pop(0)
                
                if curr:
                    curr_level.append(curr.val)
                    
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            
            if curr_level:
                ans = [curr_level] + ans
            
        return ans