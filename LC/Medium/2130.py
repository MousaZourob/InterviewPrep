# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        curr, prev = slow, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        start = head
        while prev:
            ans = max(ans, start.val + prev.val)
            start = start.next
            prev = prev.next
            
        return ans