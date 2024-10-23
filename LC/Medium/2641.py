# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root):
        if not root:
            return root
        q = deque([root])
        level_sums = []
        
        while q:
            level = 0
            for _ in range(len(q)):
                curr = q.popleft()
                level += curr.val
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            level_sums.append(level)
        
        
        root.val = 0
        q = deque([root])
        curr_level = 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                child_sum = curr.left.val if curr.left else 0
                child_sum += curr.right.val if curr.right else 0
                
                if curr.left:
                    curr.left.val = level_sums[curr_level] - child_sum
                    q.append(curr.left)
                if curr.right:
                    curr.right.val = level_sums[curr_level] - child_sum
                    q.append(curr.right) 
                
            curr_level += 1
        return root