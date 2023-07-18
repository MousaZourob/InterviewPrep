# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            prev = None
            curr = head

            while curr:
                curr.next, prev, curr = prev, curr, curr.next

            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        
        ans = ListNode()
        carry = 0
        total = 0
        while l1 or l2:
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            ans.val = total % 10
            carry = total // 10
            new = ListNode(carry)
            new.next = ans
            ans = new
            total = carry
        
        
        return ans.next if carry == 0 else ans