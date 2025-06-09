# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(curr, targetSum, curr_path):
            if not curr: return 0
            
            curr_path.append(curr.val)
            
            path_count = 0
            path_sum = 0
            
            for num in curr_path[::-1]:
                path_sum += num
                
                if path_sum == targetSum:
                    path_count += 1
            
            path_count += dfs(curr.left, targetSum, curr_path)
            path_count += dfs(curr.right, targetSum, curr_path)
            
            curr_path.pop()
            
            return path_count
            
        
        return dfs(root, targetSum, [])