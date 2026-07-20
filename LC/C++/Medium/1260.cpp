class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        std::vector<int> nums;
        std::vector<std::vector<int>> ans;

        int rows = grid.size();
        int cols = grid[0].size();

        for (const auto& row : grid) {
            nums.insert(nums.end(), row.begin(), row.end());
        }
        
        int n = nums.size();
        k %= n;

        rotate(nums.begin(), nums.end() - k, nums.end());

        for (int i = 0; i < rows; ++i) {
            ans.emplace_back(
                nums.begin() + i * cols,
                nums.begin() + (i + 1) * cols
            );
        }

        return ans;
    }
};