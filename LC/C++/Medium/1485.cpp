/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     Node *left;
 *     Node *right;
 *     Node *random;
 *     Node() : val(0), left(nullptr), right(nullptr), random(nullptr) {}
 *     Node(int x) : val(x), left(nullptr), right(nullptr), random(nullptr) {}
 *     Node(int x, Node *left, Node *right, Node *random) : val(x), left(left), right(right), random(random) {}
 * };
 */

class Solution {
    std::unordered_map<Node*, NodeCopy*> nodes;
public:
    NodeCopy* dfs(Node* curr) {
        if (!curr) return nullptr;

        if (nodes.count(curr)) return nodes[curr];

        NodeCopy* copy = new NodeCopy(curr->val);
        nodes[curr] = copy;

        copy->left = dfs(curr->left);
        copy->right = dfs(curr->right);
        copy->random = dfs(curr->random);

        return copy;
    }

    NodeCopy* copyRandomBinaryTree(Node* root) {
        return dfs(root);
    }
};