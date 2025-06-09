# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        total_sum = [0]
        
        def maxSubtreeProduct(curr):
            if not curr:
                return 0
            
            subtree_sum = (curr.val + maxSubtreeProduct(curr.left) + maxSubtreeProduct(curr.right))
            ans[0] = max(ans[0], (total_sum[0] - subtree_sum) * subtree_sum)
            return subtree_sum
        
        total_sum[0] = maxSubtreeProduct(root)
        maxSubtreeProduct(root)
        
        return ans[0] % (10**9 + 7)