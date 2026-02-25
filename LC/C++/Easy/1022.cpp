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
    int dfs(TreeNode* curr, int currVal) {
        if (curr == nullptr) {
            return 0;
        }

        currVal = (currVal << 1) | curr->val;

        if (!curr->left && !curr->right) {
            return currVal;
        }

        return dfs(curr->left, currVal) + dfs(curr->right, currVal);
    }

    int sumRootToLeaf(TreeNode* root) {
        return dfs(root, 0);
    }
};