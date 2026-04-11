class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        int n = nums.size();
        int ans = n*2;
        std::unordered_map<int, vector<int>> numIdx{};

        for (int i = 0; i < n; ++i) {
            numIdx[nums[i]].push_back(i);
            if (numIdx[nums[i]].size() < 3) {
                continue;
            }
            vector<int> v = numIdx[nums[i]];
            for (int i = 2; i < v.size(); ++i) {
                ans = min(ans, abs(v[i - 2] - v[i - 1]) + abs(v[i - 1] - v[i]) + abs(v[i] - v[i - 2]));
            }

        }

        return ans == n*2 ? -1 : ans;
    }
};