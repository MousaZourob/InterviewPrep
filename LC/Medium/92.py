# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0, head)
        curr = head
        lprev = dummy

        for i in range(left - 1):
            lprev = curr
            curr = curr.next
        
        prev = None
        for i in range(right - left + 1):
            curr.next, prev, curr = prev, curr, curr.next
        
        lprev.next.next = curr
        lprev.next = prev
        
        return dummy.next