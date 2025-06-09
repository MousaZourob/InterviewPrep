# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        lprev = dummy
        
        while True:
            k_node = self.getK(lprev, k)
            
            if not k_node:
                break
            next_group = k_node.next
            
            prev = k_node.next
            curr = lprev.next
            
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            lprev.next, lprev = k_node, lprev.next
            
        return dummy.next
    
    def getK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr