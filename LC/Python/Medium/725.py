# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
            
        size, rem = divmod(n, k)
        
        curr = head
        prev = None
        
        ans = [None] * k
        for i in range(k):
            ans[i] = curr
            
            for j in range(size + (1 if rem > 0 else 0)):
                prev = curr
                curr = curr.next
            
            if prev:
                prev.next = None
                
            if rem > 0:
                rem -= 1
        
        return ans