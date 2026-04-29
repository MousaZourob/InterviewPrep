class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        std::vector<int> nums;
        int first = grid[0][0] % x;
         for (auto& row : grid) {
            for (auto n : row) {
                if (n % x != first) return -1;
                nums.push_back(n);
            }
        }

        sort(nums.begin(), nums.end());

        int mid = nums[nums.size() / 2];

        int ans = 0;
        for (int n : nums) {
            ans += abs(n - mid) / x;
        }

        return ans;
    }
};