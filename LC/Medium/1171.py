# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0, head)
        curr = ans
        
        curr_sum = 0
        sum_to_node = {}

        while curr is not None:
            curr_sum += curr.val

            if curr_sum in sum_to_node:
                prev = sum_to_node[curr_sum]
                curr = prev.next

                p = curr_sum + curr.val
                while p != curr_sum:
                    del sum_to_node[p]
                    curr = curr.next
                    p += curr.val

                prev.next = curr.next
            else:
                sum_to_node[curr_sum] = curr

            curr = curr.next

        return ans.next