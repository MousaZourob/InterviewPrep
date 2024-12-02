# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Data:
    def __init__(self, min_node, max_node, max_size):
        self.max_node = max_node
        self.min_node = min_node
        self.max_size = max_size

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr):
            if not curr:
                return Data(inf, -inf, 0)
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            if left.max_node < curr.val < right.min_node:
                return Data(min(curr.val, left.min_node), max(curr.val, right.max_node), left.max_size + right.max_size + 1)
            else:
                return Data(-inf, inf, max(left.max_size, right.max_size))
        
        return dfs(root).max_size