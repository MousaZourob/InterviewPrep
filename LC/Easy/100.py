# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        
        if p.val != q.val:
            return False
        
        queue = [(p, q)]
        
        while queue:
            p_curr, q_curr = queue.pop(0)

            if not p_curr and not q_curr:
                continue
            else:
                if None in [p_curr, q_curr]:
                    return False
                if p_curr.val != q_curr.val:
                    return False
                
                queue.append((p_curr.left, q_curr.left))
                queue.append((p_curr.right, q_curr.right)) 

        return True