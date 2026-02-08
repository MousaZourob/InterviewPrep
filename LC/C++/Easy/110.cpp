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
public:
    bool ans = true;

    int dfs(TreeNode* curr) {
        if (curr == nullptr || ans == false) { return 0; }
        int left = dfs(curr->left);
        int right = dfs(curr->right);
        if (abs(left - right) > 1) {
            ans = false;
            return 0;
        }

        return max(left, right) + 1;
    }

    bool isBalanced(TreeNode* root) {
        dfs(root);
        return ans;
    }
};