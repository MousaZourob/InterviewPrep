# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []
        
        def dfs(curr):
            if not curr:
                return 
            
            curr.left = dfs(curr.left)
            curr.right = dfs(curr.right)
            
            if curr.val in to_delete:
                if curr.left:
                    ans.append(curr.left)
                if curr.right:
                    ans.append(curr.right)
                return None
            
            return curr
        
        root = dfs(root)
        
        if root:
            ans.append(root)
        
        return ans