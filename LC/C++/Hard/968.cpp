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
 0 covered no camera
 1 has camera
 2 not covered
 */
class Solution {
    int ans_ = 0;
    int dfs(TreeNode* curr) {
        if (!curr) return -1;

        int left = dfs(curr->left);
        int right = dfs(curr->right);

       if (left == 2 || right == 2) {
            ans_++;
            return 1;
        } else if (left == 1 || right == 1) {
            return 0;
        }
        return 2;
    }
public:
    int minCameraCover(TreeNode* root) {
        if (dfs(root) == 2) ans_++;
        return ans_;
    }
};