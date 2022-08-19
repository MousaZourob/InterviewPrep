# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def bfs(root):
            if not root:
                return 
            bfs(root.left)
            ans.append(root.val)
            bfs(root.right)
            
        bfs(root)
        return ans