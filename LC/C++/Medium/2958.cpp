class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        size_t ans = 0;
        size_t l = 0;
        std::unordered_map<size_t, int> seen{};

        for (size_t r = 0; r < nums.size(); ++r) {
            seen[nums[r]]++;

            while (seen[nums[r]] > k) {
                seen[nums[l]]--;
                l++;
            }

            ans = std::max(ans, r - l + 1);
        }

        return ans;
    }
};