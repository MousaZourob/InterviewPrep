class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int ans = 1;
        int curr_min = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] - curr_min > k) {
                ans += 1;
                curr_min = nums[i];
            }
        }

        return ans;
    }
};