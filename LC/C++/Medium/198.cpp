class Solution {
    std::unordered_map<int, int> cache;
public:
    int dfs(int i, vector<int>& nums) {
        if (cache.contains(i)) return cache[i];
        if (i >= nums.size()) return 0;

        int res = max(nums[i] + dfs(i+2, nums), dfs(i+1, nums));
        cache[i] = res;
        return res;
    }

    int rob(vector<int>& nums) {
        return dfs(0, nums);
    }
};