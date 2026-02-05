class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        vector<int> ans(int(nums.size()));
        int n = nums.size();

        for (int i = 0; i < n; ++i) {
            int index = 0;
            index = (i + nums[i]) % n;
            if (nums[i] < 0) {
                index = (index + n) % n;
            }
            ans[i] = nums[index];
        }

        return ans;
    }
};