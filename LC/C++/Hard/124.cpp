/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int ans_ = -INT_MAX;
public:
    int dfs(TreeNode* curr) {
        if (curr == nullptr) { return 0; }

        int left = curr->left == nullptr ? 0 : dfs(curr->left);
        if (left < 0) {
            left = 0;
        }
        
        int right = curr->right == nullptr ? 0 : dfs(curr->right);
        if (right < 0) {
            right = 0;
        }

        int res = left + right + curr->val;
        ans_ = max(ans_, res);
        return max(left, right) + curr->val;
    }

    int maxPathSum(TreeNode* root) {
        dfs(root);
        return ans_;
    }
};