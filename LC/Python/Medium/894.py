# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = { 0: [], 1 : [TreeNode()] }
        
        def dfs(num):
            if num in dp:
                return dp[num]
            
            res = []
            for l in range(1, num, 2):
                left = dfs(l)
                right = dfs(num - l - 1)
                
                for l in left:
                    for r in right:
                        root = TreeNode(0, l, r)
                        res.append(root)
            
            dp[num] = res
            return res
            
        return dfs(n)