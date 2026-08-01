class Solution {
    std::vector<std::vector<int>> cache;
public:
    int dfs(vector<int>& nums, int l, int r) {
        if (l > r) return 0;

        if (cache[l][r] != INT_MIN) return cache[l][r];

        int left = nums[l] - dfs(nums, l + 1, r);
        int right = nums[r] - dfs(nums, l, r - 1);

        return cache[l][r] = std::max(left, right);
    }

    bool predictTheWinner(vector<int>& nums) {
        std::size_t n = nums.size(); 
        cache.resize(n, std::vector(n, INT_MIN));

        return dfs(nums, 0, n - 1) >= 0;
    }
};