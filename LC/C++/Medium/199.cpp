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
    vector<int> rightSideView(TreeNode* root) {
        std::vector<int> ans{};
        std::queue<TreeNode*> q{};
        
        if (root) q.push(root);

        while (!q.empty()) {
            int last = -1;
            size_t n = q.size();

            while (n-- > 0) {
                TreeNode* curr = q.front();
                q.pop();

                last = curr->val;

                if (curr->left) q.push(curr->left);
                if (curr->right) q.push(curr->right);
            }

            ans.push_back(last);
        }

        return ans;
    }
};