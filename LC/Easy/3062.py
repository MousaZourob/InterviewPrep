# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        ans = 0
        
        while head:
            even = head.val
            odd = head.next.val
            
            if even > odd:
                ans += 1
            else:
                ans -= 1
            
            head = head.next.next
        
        if ans > 0:
            return "Even"
        elif ans < 0:
            return "Odd"
        
        return "Tie"