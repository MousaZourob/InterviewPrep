"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(curr):
            if not curr:
                return
           
            for child in curr.children:
                dfs(child)
            ans.append(curr.val)
        
        dfs(root)
        return ans
