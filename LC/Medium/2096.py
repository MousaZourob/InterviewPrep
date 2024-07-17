# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(curr, target):
            if not curr:
                return None
            if curr.val == target:
                return path
            
            path.append("L")
            res = dfs(curr.left, target)
            if res: return res
            
            path.pop()
            path.append("R")
            res = dfs(curr.right, target)
            if res: return res
            
            path.pop()
            return None
            
        path = []
        path_to_s = dfs(root, startValue)
        path = []
        path_to_d = dfs(root, destValue)
        
        i_s = 0
        i_d = 0
        
        for i in range(min(len(path_to_s), len(path_to_d))):
            if path_to_s[i_s] != path_to_d[i_d]:
                break
            i_s += 1
            i_d += 1
        ans = ["U"] * len(path_to_s[i_s:]) + path_to_d[i_d:]
        
        return "".join(ans)
        