class Solution {
    std::unordered_map<int, int> nodes;

    int dfs(int i, int curr) {
        curr += nodes[i];

        // if leaf return res
        int depth = i / 10;
        int pos = i % 10;

        int leftI = (depth + 1) * 10 + (pos * 2 - 1);
        int rightI = (depth + 1) * 10 + (pos * 2);

        if (!nodes.contains(leftI) && !nodes.contains(rightI)) {
            return curr;
        }

        // dfs left and dfs right
        int res = 0;
        if (nodes.contains(leftI)) {
            res += dfs(leftI, curr);
        }
        if (nodes.contains(rightI)) {
            res += dfs(rightI, curr);
        }

        // return result
        return res;
    }

public:
    int pathSum(vector<int>& nums) {
        for (auto num : nums) {
            nodes[num / 10] = num % 10;
        }

        return dfs(11, 0);
    }
};