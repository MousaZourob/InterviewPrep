# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def dfs(curr, curr_path):
            if not curr:
                return
            
            curr_path.append(str(curr.val))
            if not curr.right and not curr.left:
                ans.append("->".join(curr_path))
            else:
                dfs(curr.left, curr_path)
                dfs(curr.right, curr_path)
            
            curr_path.pop()
        
        dfs(root, [])
        
        return ans