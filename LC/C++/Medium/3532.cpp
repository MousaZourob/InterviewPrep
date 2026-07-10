class Solution {
public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        std::vector<int> components(n, 0);
        int currComponent = 0;
        for (size_t i{1}; i < nums.size(); ++i) {
            if (nums[i] - nums[i-1] > maxDiff) {
                currComponent++;
            }
            components[i] = currComponent;
        }

        std::vector<bool> ans(queries.size(), false);
        for (size_t i{0}; i < queries.size(); i++) {
            if (components[queries[i][0]] == components[queries[i][1]]) ans[i] = true;
        }

        return ans;
    }
};