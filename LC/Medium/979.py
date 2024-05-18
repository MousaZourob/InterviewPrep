class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(curr):
            if not curr: return 0

            left_coins = dfs(curr.left)
            right_coins = dfs(curr.right)

            ans[0] += abs(left_coins) + abs(right_coins)

            return curr.val - 1 + left_coins + right_coins

        dfs(root)

        return ans[0]