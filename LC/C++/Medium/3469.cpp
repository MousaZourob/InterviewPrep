class Solution {
    std::vector<std::vector<int>> cache;
    int dfs(vector<int>& nums, int i, int carryI) {
        if (nums.size() - i <= 1) {
            int num = (i < nums.size()) ? nums[i] : INT_MIN;
            return max(nums[carryI], num);
        }
        if (cache[i][carryI] != -1) return cache[i][carryI];

        int c1 = dfs(nums, i + 2, i + 1) + std::max(nums[carryI], nums[i]);
        int c2 = dfs(nums, i + 2, i) + std::max(nums[carryI], nums[i + 1]);
        int c3 = dfs(nums, i + 2, carryI) + std::max(nums[i], nums[i + 1]);

        return cache[i][carryI] = std::min({c1, c2, c3});
    }
public:
    int minCost(vector<int>& nums) {
        cache.assign(nums.size(), vector<int>(nums.size(), -1));
        return dfs(nums, 1, 0);
    }
};