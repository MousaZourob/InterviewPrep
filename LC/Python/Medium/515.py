# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        ans = []
        
        while q:
            n = len(q)
            curr_max = -inf

            for _ in range(n):
                curr = q.pop(0)
                if curr:
                    curr_max = max(curr_max, curr.val)
                    
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                
            if curr_max != -inf:
                ans.append(curr_max)
        
        
        return ans