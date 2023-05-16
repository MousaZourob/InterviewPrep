# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            first = curr
            second = curr.next
            
            second.next, first.next, prev.next = first, second.next, second
            
            prev, curr = first, first.next
        
        return dummy.next