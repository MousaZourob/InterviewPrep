class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return 

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next       

        head1, head2 = head, prev
        while head2.next:
            head1.next, head1 = head2, head1.next
            head2.next, head2 = head1, head2.next