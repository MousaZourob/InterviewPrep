# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root, 0)])
        cols = defaultdict(list)
        min_col = 0
        max_col = 0
        
        while q:
            n = len(q)
            for _ in range(n):
                curr, col = q.popleft()
                cols[col].append(curr.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                
                if curr.left:
                    q.append((curr.left, col - 1))
                if curr.right:
                    q.append((curr.right, col + 1))
            
        return [cols[i] for i in range(min_col, max_col+1)]