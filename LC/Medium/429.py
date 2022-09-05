"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = [root]
        ans = []
        
        while q:
            curr_level = []
            
            for i in range(len(q)):
                curr = q.pop(0)
                
                if curr:
                    curr_level.append(curr.val)
                    
                    for node in curr.children:
                        q.append(node)
            
            if curr_level:
                ans.append(curr_level)
                
        return ans
            