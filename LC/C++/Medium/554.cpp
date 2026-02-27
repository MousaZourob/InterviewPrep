class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        int n = wall.size();
        std::unordered_map<long long, int> counts{};
        int ans = n;
        
        for (auto& row : wall) {
            long long sum = 0;
            for (int i = 0; i < row.size() - 1; ++i) {
                sum += row[i];
                ++counts[sum];
                ans = std::min(ans, n - counts[sum]);
            }
        }

        return ans;
    }
};