# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Data:
    def __init__(self, min_node, max_node, max_sum):
        self.min_node = min_node
        self.max_node = max_node
        self.max_sum = max_sum

    def __str__(self):
        return f"Data(min_node={self.min_node}, max_node={self.max_node}, max_sum={self.max_sum})"

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(curr):
            if not curr:
                return Data(inf, -inf, 0)
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            if left.max_node < curr.val < right.min_node:
                ans[0] = max(ans[0], curr.val + left.max_sum + right.max_sum)
                return Data(min(curr.val, left.min_node), max(curr.val, right.max_node), curr.val + left.max_sum + right.max_sum)
            else:
                return Data(-inf, inf, max(left.max_sum, right.max_sum))
        
        dfs(root)
        return ans[0]