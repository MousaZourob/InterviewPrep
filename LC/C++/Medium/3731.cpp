class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        int low = INT_MAX;
        int high = INT_MIN;
        unordered_set<int> seen{};

        for (int i = 0; i < nums.size(); ++i) {
            low = std::min(low, nums[i]);
            high = std::max(high, nums[i]);
            seen.insert(nums[i]);
        }

        std::vector<int> ans{};
        for (int i = low + 1; i < high; ++i) {
            if (!seen.contains(i)) ans.push_back(i);
        }

        return ans;
    }
};