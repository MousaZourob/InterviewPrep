class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        int n = nums.size();
        int small = 0;
        int large = 0;
        std::vector<int> ans{};

        for (auto& num : nums) {
            if (num > target) large++;
            else if (num < target) small++;
        }

        for (int i = small; i < n - large; ++i) {
            ans.push_back(i);
        }

        return ans;
    }
};