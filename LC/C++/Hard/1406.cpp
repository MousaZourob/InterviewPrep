class Solution {
    std::vector<int> cache{};
    int n;

    int dfs(vector<int>& nums, int i) {
        if (i >= n) return 0;

        if (cache[i] != INT_MIN) return cache[i];

        int best = nums[i] - dfs(nums, i + 1);

        if (i + 1 < n)
            best = max(best, nums[i] + nums[i + 1] - dfs(nums, i + 2));

        if (i + 2 < n)
            best = max(best, nums[i] + nums[i + 1] + nums[i + 2] - dfs(nums, i + 3));

        return cache[i] = best;
    }

public:
    string stoneGameIII(vector<int>& stoneValue) {
        n = stoneValue.size();
        cache.resize(n, INT_MIN);

        int val = dfs(stoneValue, 0);
        
        if (val > 0) return "Alice";
        else if (val < 0) return "Bob";
        return "Tie";
    }
};