# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        parent = {}
        q = [root]

        while q:
            n = len(q)
            for _ in range(n):
                p = q.pop(0)

                if p.left:
                    parent[p.left.val] = p
                    q.append(p.left)

                if p.right:
                    parent[p.right.val] = p
                    q.append(p.right)

        visited = {}
        q.append(target)
        while k > 0 and q:
            n = len(q)

            for _ in range(n):
                p = q.pop(0)

                visited[p.val] = 1

                if p.left and p.left.val not in visited:
                    q.append(p.left)

                if p.right and p.right.val not in visited:
                    q.append(p.right)

                if p.val in parent and parent[p.val].val not in visited:
                    q.append(parent[p.val])

            k -= 1

        while q:
            ans.append(q.pop(0).val)

        return ans