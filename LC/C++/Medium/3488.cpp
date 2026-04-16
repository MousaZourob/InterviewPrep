class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        std::unordered_map<int, vector<int>> seen;
        for (int i = 0; i < n; ++i) {
            seen[nums[i]].push_back(i);
        }

        vector<int> ans;
        for (int q : queries) {
            vector<int>& indices = seen[nums[q]];
            if (indices.size() > 1) {
                int pos = lower_bound(indices.begin(), indices.end(), q) - indices.begin();
                int ni = indices.size();
                int res = INT_MAX;

                for (int d : {-1, 1}) {
                    int lin = abs(indices[(pos + d + ni) % ni] - q);
                    res = min(res, min(lin, n - lin));
                }

                ans.push_back(res);
            } else {
                ans.push_back(-1);
            }
        }

        return ans;
    }
};