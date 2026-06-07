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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        std::unordered_map<int, TreeNode*> nodes;
        std::unordered_set<int> children;

        for (auto& desc : descriptions) {
            int parent = desc[0];
            int child = desc[1];
            int isLeft = desc[2];
            
            if (!nodes.count(parent))
                nodes[parent] = new TreeNode(parent);

            if (!nodes.count(child))
                nodes[child] = new TreeNode(child);

            if (isLeft) {
                nodes[parent]->left = nodes[child];
            } else {
                nodes[parent]->right = nodes[child];
            }
            children.insert(child);
        }

        for (auto& desc: descriptions) {
            if (!children.contains(desc[0])) {
                return nodes[desc[0]];
            }
        }

        return nullptr;
    }
};