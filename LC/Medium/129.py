# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:     
        def dfs(curr, curr_sum):
            if not curr:
                return 0
            
            curr_sum = curr_sum*10 + curr.val
            if not curr.right and not curr.left:
                return curr_sum
            else:
                return dfs(curr.left, curr_sum) + dfs(curr.right, curr_sum)
            
        return dfs(root, 0)