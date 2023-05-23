# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(-1, None)
        ans = curr
        carry = 0
        
        while l1 or l2:
            temp = 0
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            
            temp += carry
            carry = temp // 10   
            
            curr.next = ListNode(temp % 10)
            curr = curr.next 
        
        if carry == 1:
            curr.next = ListNode(1)
        
        return ans.next