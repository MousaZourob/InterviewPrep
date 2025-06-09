class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next     
        
        head1 = head
        while prev.next:
            head1.next, head1 = prev, head1.next
            prev.next, prev = head1, prev.next