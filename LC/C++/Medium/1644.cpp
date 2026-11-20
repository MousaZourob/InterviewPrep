/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    int found = 0;

    TreeNode* dfs(TreeNode* curr, TreeNode* p, TreeNode* q) {
        if (curr == nullptr) return nullptr;

        TreeNode* left = dfs(curr->left, p, q);
        TreeNode* right = dfs(curr->right, p, q);

        if (left && right) return curr;
        else if (curr == p || curr == q) {
            found++;
            return curr;
        }

 
        return left ? left : right;
    }

public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* lca = dfs(root, p, q);

        return found == 2 ? lca : nullptr;
    }
};