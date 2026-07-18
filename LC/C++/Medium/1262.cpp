class Solution {
    std::vector<std::vector<int>> cache_;
    int dfs(vector<int>& nums, int i, int r) {
        if (i == nums.size()) return r == 0 ? 0 : INT_MIN;
        if (cache_[i][r] != -1) return cache_[i][r];

        int skip = dfs(nums, i + 1, r);

        int need = ((r - nums[i]) % 3 + 3) % 3;
        int pick = nums[i] + dfs(nums, i + 1, need);

        return cache_[i][r] = max(skip, pick); 
    }

public:
    int maxSumDivThree(vector<int>& nums) {
        cache_.assign(nums.size(), vector<int>(3, -1));
        return dfs(nums, 0, 0);
    }
};