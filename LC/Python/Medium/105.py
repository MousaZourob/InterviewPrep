# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(pre, inn):
            if not pre or not inn:
                return None
            
            root = TreeNode(pre[0])
            mid = inn.index(root.val)
            
            root.left = dfs(pre[1:mid+1], inn[:mid])
            root.right = dfs(pre[mid+1:], inn[mid+1:])
            
            return root

        return dfs(preorder, inorder)