class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int ans = n;
        int windowStart = 0;

        for (int windowEnd = 0; windowEnd < n; ++windowEnd) {
            while (windowStart < n && nums[windowStart] <= static_cast<long long>(nums[windowEnd]) * k) {
                ++windowStart;
            }

            ans = min(ans, n - (windowStart - windowEnd));
        }
        
        return ans;
    }
};