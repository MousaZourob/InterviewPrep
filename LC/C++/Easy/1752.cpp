class Solution {
public:
    bool check(vector<int>& nums) {
        int n = nums.size();
        int cliff = 0;

        for (size_t i = 0; i < n; ++i) {
            if (nums[i] > nums[(i + 1) % n]) {
                cliff++;
                if (cliff > 1) {
                    return false;
                }
            }
        }

        return true;
    }
};
