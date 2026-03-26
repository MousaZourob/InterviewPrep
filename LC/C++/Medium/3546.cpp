class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        long long totalSum = 0;

        for (auto& r : grid) {
            for (auto& c : r) {
                totalSum += c;
            }
        }

        if (totalSum % 2) return false;
        totalSum = totalSum / 2;
        long long target = 0;
        for (auto& r : grid) {
            for (auto& c : r) {
                target += c;
            }
            if (totalSum == target) return true;
        }

        target = 0;
        for (int i = 0; i < grid[0].size(); ++i) {
            for (int j = 0; j < grid.size(); ++j) {
                target += grid[j][i];
            }
            if (totalSum == target) return true;
        }

        return false;
    }
};