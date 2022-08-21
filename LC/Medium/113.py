# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(curr, target, curr_path):
            if not curr:
                return
            
            curr_path.append(curr.val)
            
            if curr.val == target and not curr.right and not curr.left:
                ans.append(list(curr_path))
            else:
                dfs(curr.right, target - curr.val, curr_path)
                dfs(curr.left, target - curr.val, curr_path)
            
            curr_path.pop()
        
        dfs(root, targetSum, [])
        
        return ans