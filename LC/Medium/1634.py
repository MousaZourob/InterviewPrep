# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        ans = PolyNode()
        curr = ans
        
        while poly1 and poly2:
            if poly1.power > poly2.power:
                new_node = PolyNode(poly1.coefficient, poly1.power)
                poly1 = poly1.next
                
                curr.next = new_node
                curr = curr.next
                
            elif poly2.power > poly1.power:
                new_node = PolyNode(poly2.coefficient, poly2.power)
                poly2 = poly2.next
                
                curr.next = new_node
                curr = curr.next
            else:
                new_node = PolyNode(poly1.coefficient + poly2.coefficient, poly1.power)
                poly1 = poly1.next
                poly2 = poly2.next
                
                if new_node.coefficient == 0:
                    continue

                curr.next = new_node
                curr = curr.next

        if poly1:
            curr.next = poly1
        if poly2:
            curr.next = poly2
        
        return ans.next