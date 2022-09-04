# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)

        def dfs(node, col, row):
            if not node:
                return
            
            nodes[col].append((row, node.val))
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)
            
        
        dfs(root, 0, 0)
        
        res = []
        for col in sorted(nodes.keys()):
            res.append([val for _, val in sorted(nodes[col])])
        return res