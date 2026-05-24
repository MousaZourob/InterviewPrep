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
    vector<vector<int>> ans_{};
    vector<int> curr_;
public:
    void dfs(TreeNode* curr, int target) {
        if (curr == nullptr) return;

        curr_.push_back(curr->val);
        if (curr->left == nullptr && curr->right == nullptr && curr->val == target) {
            ans_.push_back(curr_);
            curr_.pop_back();
            return;
        }

        dfs(curr->left, target - curr->val);
        dfs(curr->right, target - curr->val);
        curr_.pop_back();
        return;
    }

    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        dfs(root, targetSum);

        return ans_;
    }
};