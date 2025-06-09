# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = defaultdict(int)
        
        curr = head
        while curr:
            count[curr.val] += 1
            curr = curr.next
        
        ans = ListNode()
        
        curr = ans
        for v in count.values():
            curr.next = ListNode(v)
            curr = curr.next
        
        return ans.next
         