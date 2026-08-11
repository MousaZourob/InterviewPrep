class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int ans = nums[0];
        std::unordered_set<int> seen(nums.begin(), nums.end());

        for (size_t i{1}; i < nums.size(); ++i) {
            if (nums[i] == nums[i - 1] + 1) {
                ans += nums[i];
            }
            else {
                break;
            }
        }

        while (seen.count(ans)) {
            ans++;
        }

        return ans;
    }
};