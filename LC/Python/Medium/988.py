# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = [chr(ord('z')+1)]
    
        def dfs(curr, word):
            if not curr: return
            
            word.append(chr(curr.val + ord('a')))
    
            if not curr.left and not curr.right:
                ans[0] = min(ans[0], ''.join(word[::-1]))
                
            dfs(curr.left, word)
            dfs(curr.right, word)
            
            word.pop()
            
        dfs(root, [])
        
        return ans[0]