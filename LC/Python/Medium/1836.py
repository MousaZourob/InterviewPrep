# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if not head.next:
            return head

        found = defaultdict(int)
        curr = head
        while curr:
            found[curr.val] += 1
            curr = curr.next
            
        curr = head
        ans = ListNode(-1, curr)
        prev = ans
        while curr:
            if found[curr.val] > 1:
                prev.next = prev.next.next
            else:
                prev = prev.next
            curr = curr.next
                
        return ans.next