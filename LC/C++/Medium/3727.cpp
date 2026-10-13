class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        int n = nums.size();
        for (auto& num : nums) {
            num *= num;
        }
        std::ranges::sort(nums);
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += (i < n / 2) ? -nums[i] : nums[i];
        }
        return ans;
    }
};