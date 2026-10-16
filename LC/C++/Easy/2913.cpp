class Solution {
public:
    int sumCounts(vector<int>& nums) {
        int ans = 0;

        for (size_t i = 0; i < nums.size(); ++i) {
            std::unordered_set<int> s{};
            for (size_t j = i; j < nums.size(); ++j) {
                s.insert(nums[j]);
                ans += s.size() * s.size();
            }
        }

        return ans;
    }
};