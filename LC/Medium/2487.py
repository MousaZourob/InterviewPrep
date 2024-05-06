# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, curr):
        prev = None
        
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev
        
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)

        max_val = 0
        prev = None
        curr = head

        while curr:
            if curr.val < max_val:
                prev.next = curr.next
            else:
                max_val = curr.val
                prev = curr
            curr = curr.next
        
        return self.reverse(head)        
        