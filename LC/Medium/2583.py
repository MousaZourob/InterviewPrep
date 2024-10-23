# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        heap = []
        q = [root]
        
        while q:
            level_sum = 0
            for _ in range(len(q)):
                curr = q.pop(0)
                level_sum += curr.val
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
            heappush(heap, level_sum)
        
        k = len(heap) - k
        if k < 0:
            return -1 

        while k > 0:
            heappop(heap)
            k -= 1
        
        return heap[0]
