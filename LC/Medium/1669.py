# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        new_a = None
        new_b = None
        i = 0

        while curr:
            if i == a-1:
                new_a = curr
            if i == b+1:
                new_b = curr
            curr = curr.next
            i += 1
        
        new_a.next = list2
        while list2.next:
            list2 = list2.next
        
        list2.next = new_b
        
        return list1