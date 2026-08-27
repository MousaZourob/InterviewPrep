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
     TreeNode* dfs(TreeNode* curr, TreeNode* p, TreeNode* q) {
        if (curr == nullptr || curr == p || curr == q) {
            return curr;
        }

        TreeNode* l = dfs(curr->left, p, q);
        TreeNode* r = dfs(curr->right, p, q);

        if (l && r) {
            return curr;
        }

        return l != nullptr ? l : r;
     }
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return dfs(root, p, q);
    }
};