# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        s1 = set()
        s2 = set()
        
        def dfs(curr, tree):
            if not curr:
                return 
            
            dfs(curr.left, tree)
            if tree:
                s1.add(curr.val)
            else:
                s2.add(curr.val)   
            dfs(curr.right, tree)
            
        dfs(root1, 1)
        dfs(root2, 0)
                
        for num in s1:
            if target - num in s2:
                return True
        
        return False
