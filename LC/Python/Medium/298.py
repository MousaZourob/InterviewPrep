# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(curr, prev, length):
            if not curr:
                return length
            
            if prev and curr.val == prev.val + 1:
                length += 1
            else:
                length = 1
            
            left_max = dfs(curr.left, curr, length)
            right_max = dfs(curr.right, curr, length)
            
            return max(length, left_max, right_max)

        return dfs(root, None, 0)
