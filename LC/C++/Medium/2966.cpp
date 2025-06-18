class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        ans.reserve(nums.size() / 3);

        for (int i = 0; i < nums.size(); i += 3) {
            if (nums[i + 2] - nums[i] > k) {
                return {};
            }
            ans.emplace_back(vector<int>{nums[i], nums[i + 1], nums[i + 2]});
        }

        return ans;
    }
};