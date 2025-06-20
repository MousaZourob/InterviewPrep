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
    unordered_set<int> seen;
    int dfs(TreeNode* curr) {
        if (curr == nullptr) {
            return 0;
        }
        int res = dfs(curr->left) + dfs(curr->right) + curr->val;
        seen.insert(res);
        return res;
    }

    bool checkEqualTree(TreeNode* root) {
        int total = dfs(root->left) + dfs(root->right) + root->val;
        return total % 2 == 0 && seen.count(total / 2);
    }
};