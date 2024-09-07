# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(curr_node, curr_head):
            if not curr_head:
                return True
            if not curr_node or curr_node.val != curr_head.val:
                return False
            
            return dfs(curr_node.left, curr_head.next) or dfs(curr_node.right, curr_head.next)
        
        if not root:
            return False
        if dfs(root, head):
            return True
    
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)