# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')
        max_level = 0
        q = collections.deque()
        q.append(root)
        
        curr_level = 0
        while q:
            curr_level += 1
            level_size = len(q)
            curr_sum = 0
            
            for i in range(level_size):
                curr = q.popleft()
                
                if curr:
                    curr_sum += curr.val
                    
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)

            
            if max_sum < curr_sum:
                max_level = curr_level
                max_sum = curr_sum
         
        return max_level