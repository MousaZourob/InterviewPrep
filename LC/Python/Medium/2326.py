# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * n for _ in range(m)]
        i, j = 0, -1
        dirr = 1
        
        while 0 < m*n and head:
            for _ in range(n):
                if not head:
                    return ans
                j += dirr
                ans[i][j] = head.val
                head = head.next
            m -= 1
            
            for _ in range(m):
                if not head:
                    return ans
                i += dirr
                ans[i][j] = head.val
                head = head.next
            n -= 1
            
            dirr *= -1
        
        return ans