# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        is_child = set()
        nodes = {}
        
        for parent, child, left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            
            if child not in nodes:
                nodes[child] = TreeNode(child)
            
            if left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            
            is_child.add(child)
            
        for parent, _, _ in descriptions:
            if parent not in is_child:
                return nodes[parent]
        
        return None