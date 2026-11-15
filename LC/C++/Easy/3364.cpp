class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int n = nums.size();
        int ans = INT_MAX;

        for (int len = l; len <= r; ++len) {
            int curr = 0;
            for (int i = 0; i < n; ++i) {
                curr += nums[i];
                if (i >= len) curr -= nums[i - len];
                if (i >= len - 1 && curr > 0 && curr < ans) ans = curr;
            }
        }

        return ans != INT_MAX ? ans : -1;
    }
};