# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        curr = head
        prev = curr
        curr = curr.next
        
        while curr:
            gcd_val = gcd(curr.val, prev.val)
            new_node = ListNode(gcd_val, curr)
            prev.next = new_node
            prev = curr
            curr = curr.next       
            
        return head